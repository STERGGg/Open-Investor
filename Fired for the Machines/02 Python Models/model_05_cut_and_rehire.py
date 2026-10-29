"""
MODEL 05  Have they done this before?
1. Meta's headcount at the points it reports (end of 2021, the third quarter of 2022 peak, year ends
   2022 to 2024, and the third quarters of 2025 and 2026), from its 10-K filings and quarterly results,
   with the announced layoff rounds marked. The model measures how much of the 2022 to 2023 fall was
   hired back before the 2026 cuts began, and how long it took.
2. Microsoft's headcount at 30 June each year from its 10-K filings, 2019 to 2026, against the cuts
   it announced. Fiscal 2026 ran from July 2025 to June 2026 and included the July 2025 round of
   about 9,000. If headcount fell by only 5,000 over a year in which at least 9,000 were laid off,
   then Microsoft hired at least 4,000 more people than it lost through other leavers, which shows
   that it was swapping people as well as shedding them.
"""
from common import *

style(); h = hand()
mh = pd.Series({pd.Timestamp("2021-12-31"): h["meta_headcount_2021q4"], pd.Timestamp("2022-09-30"): h["meta_headcount_2022q3"],
                pd.Timestamp("2022-12-31"): h["meta_headcount_2022q4"], pd.Timestamp("2023-12-31"): h["meta_headcount_2023q4"],
                pd.Timestamp("2024-12-31"): h["meta_headcount_2024q4"], pd.Timestamp("2025-09-30"): h["meta_headcount_2025q3"],
                pd.Timestamp("2026-09-30"): h["meta_headcount_2026q3"]})
peak, trough, rebound, now = mh["2022-09-30"], mh["2023-12-31"], mh["2025-09-30"], mh["2026-09-30"]
ms = pd.Series({y: h[f"msft_headcount_{y}"] for y in range(2019, 2027)})
res = pd.Series({"meta_peak_2022": peak, "meta_trough_2023": trough, "meta_fall": peak - trough, "meta_fall_pct": (trough / peak - 1) * 100,
                 "meta_rehired": rebound - trough, "meta_share_of_fall_rehired_pct": (rebound - trough) / (peak - trough) * 100,
                 "months_trough_to_rebound": 21, "meta_2026_fall": rebound - now, "meta_2026_fall_pct": (now / rebound - 1) * 100,
                 "meta_now_vs_2021": (now / mh["2021-12-31"] - 1) * 100,
                 "msft_change_fy26": ms[2026] - ms[2025], "msft_min_net_hires_fy26": 9000 + (ms[2026] - ms[2025]),
                 "msft_change_since_2022": ms[2026] - ms[2022], "msft_buyout_share_of_staff_pct": h["msft_buyout_eligible"] / ms[2026] * 100})
save_table(mh.to_frame("meta_headcount"), "m05_meta_headcount"); save_table(ms.to_frame("msft_headcount"), "m05_msft_headcount"); save_table(res.round(1).to_frame("value"), "m05_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.3, 1]})
ax = axes[0]
ax.plot(mh.index, mh.values / 1000, color=BLUE, marker="o", lw=2)
for d, v in mh.items():
    off = {"2022-09-30": (-25, 1.3), "2022-12-31": (45, 1.0)}.get(d.strftime("%Y-%m-%d"), (0, 1.3))
    ax.text(d + pd.Timedelta(days=off[0]), v / 1000 + off[1], f"{v / 1000:.1f}k", ha="center", fontsize=8)
for d, txt, y in (("2022-11-09", "11,000 cut", 61), ("2023-03-14", "10,000 cut", 57), ("2026-04-23", "8,000 cut and\n6,000 roles\ncancelled", 57)):
    ax.axvline(pd.Timestamp(d), color=RED, ls=":", lw=1)
    ax.text(pd.Timestamp(d) + pd.Timedelta(days=12), y, txt, fontsize=7.5, color=RED)
ax.annotate("", xy=(pd.Timestamp("2025-09-30"), rebound / 1000 - 3), xytext=(pd.Timestamp("2023-12-31"), trough / 1000 - 3),
            arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.3))
ax.text(pd.Timestamp("2024-11-01"), trough / 1000 - 6.5, f"+{(rebound - trough) / 1000:.1f}k hired back", fontsize=8, color=GREEN, ha="center")
ax.set_ylim(52, 93); ax.set_ylabel("Meta employees, thousand"); ticks = [d for d in mh.index if d.strftime("%Y-%m-%d") != "2022-12-31"]
ax.set_xticks(ticks); ax.set_xticklabels([d.strftime("%b %y") for d in ticks], fontsize=8)
ax.set_title("Meta cut, rehired, and is cutting again", fontsize=10.5)
ax = axes[1]
cols = [GREY] * 3 + [BLUE] * 4 + [RED]
ax.bar(ms.index, ms.values / 1000, color=cols, width=0.65)
for y, v in ms.items():
    ax.text(y, v / 1000 + 3, f"{v / 1000:.0f}k", ha="center", fontsize=8)
ax.text(2019, 245, "About 15,000 laid off in 2025 and\n4,800 in July 2026, yet 223,000 remain", fontsize=7.5, color=INK2, ha="left")
ax.set_ylim(0, 270); ax.set_ylabel("Microsoft employees at 30 June, thousand"); ax.grid(axis="x", visible=False); ax.set_xticks(list(ms.index))
ax.tick_params(axis="x", labelsize=8)
ax.set_title("Microsoft's cuts barely dent the total", fontsize=10.5)
finish(fig, "Figure 5: The last round of 'efficiency' was largely hired back",
       "author's model 05; Meta and Microsoft 10-K filings and quarterly results; Semafor (2023); SiliconANGLE (Apr 2026); TechRepublic (2025); Axios (Oct 2026).", "fig05_cut_and_rehire.png")
print(mh); print(res.round(1))
