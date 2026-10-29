"""
MODEL 01  One week in October
Daily closing prices from Nasdaq via OpenBB for Meta (META), Microsoft (MSFT), Barclays (its New
York listed shares, BCS) and the Nasdaq 100 tracker (QQQ), indexed to 100 on 30 September 2026.
Marked on the chart:
  21 Oct after the close   Meta's third quarter results, capex raised, free cash flow negative
  22 Oct                   Barclays' results and the 5,000 job cuts
  26 Oct                   Meta's equity raise and Microsoft's buyout offer to 60,000 staff
The second panel is each share's return so far in 2026 and over the five trading days from
21 to 26 October.
"""
from common import *

style(); px = prices()
base = px.loc[:"2026-09-30"].iloc[-1]
w = px.loc["2026-09-30":] / base * 100
ytd = (px.iloc[-1] / px.loc[:"2025-12-31"].iloc[-1] - 1) * 100
week = (px.iloc[-1] / px.loc[:"2026-10-21"].iloc[-1] - 1) * 100
res = pd.DataFrame({"ytd_2026_pct": ytd, "from_21_to_26_oct_pct": week, "last_close": px.iloc[-1]})
res.loc["META", "drop_on_22_oct_pct"] = (px.loc["2026-10-22", "META"] / px.loc["2026-10-21", "META"] - 1) * 100
res.loc["META", "peak_close_oct"] = px.loc["2026-10-01":, "META"].max()
save_table(res.round(2), "m01_returns")

names = {"META": "Meta", "MSFT": "Microsoft", "BCS": "Barclays", "QQQ": "Nasdaq 100"}
cols = {"META": BLUE, "MSFT": GREEN, "BCS": VIOLET, "QQQ": GREY}
fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.6, 1]})
ax = axes[0]
for c in ("QQQ", "MSFT", "BCS", "META"):
    ax.plot(w.index, w[c], color=cols[c], lw=2.2 if c == "META" else 1.6, label=names[c])
for d, txt, y in (("2026-10-22", "Meta results,\nBarclays cuts", 108), ("2026-10-26", "Meta raise,\nMicrosoft\nbuyouts", 108)):
    ax.axvline(pd.Timestamp(d), color=INK2, ls=":", lw=1)
    ax.text(pd.Timestamp(d) - pd.Timedelta(hours=8), y, txt, fontsize=7.2, color=INK2, ha="right", va="top")
ax.set_ylim(84, 109)
ax.set_ylabel("Share price, 30 Sep 2026 = 100"); ax.legend(fontsize=8, loc="lower left")
ax.set_xticks(pd.date_range("2026-10-01", "2026-10-26", freq="5D")); ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d %b"))
ax.set_title("Meta's October rally vanished in two days", fontsize=10.5)
ax = axes[1]
order = ["META", "MSFT", "BCS", "QQQ"]
y = np.arange(len(order))
ax.barh(y + 0.18, ytd[order], 0.36, color=[cols[c] for c in order], label="2026 so far")
ax.barh(y - 0.18, week[order], 0.36, color=[cols[c] for c in order], alpha=0.45, label="21 to 26 October")
for i, c in enumerate(order):
    ax.text(ytd[c] + (0.6 if ytd[c] >= 0 else -0.6), i + 0.18, f"{ytd[c]:+.0f}%", va="center", ha="left" if ytd[c] >= 0 else "right", fontsize=8)
    ax.text(week[c] + (0.6 if week[c] >= 0 else -0.6), i - 0.18, f"{week[c]:+.1f}%", va="center", ha="left" if week[c] >= 0 else "right", fontsize=8, color=INK2)
ax.axvline(0, color=INK2, lw=0.8); ax.set_yticks(y); ax.set_yticklabels([names[c] for c in order])
lim = max(abs(ytd).max(), abs(week).max()) + 12
ax.set_xlim(-lim, lim); ax.set_xlabel("Share price change, %"); ax.legend(fontsize=7.5, loc="upper right"); ax.grid(axis="y", visible=False); ax.set_ylim(3.7, -0.7)
ax.set_title("This year and this week", fontsize=10.5)
finish(fig, "Figure 1: The market punished Meta's spending, not Microsoft's cuts",
       "author's model 01; Nasdaq daily closing prices via OpenBB, to 26 October 2026.", "fig01_the_week.png")
print(res.round(2))
