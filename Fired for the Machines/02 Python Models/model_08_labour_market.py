"""
MODEL 08  What the official US jobs data shows
All from the Bureau of Labor Statistics public API (seasonally adjusted, monthly to September 2026,
JOLTS to August 2026).
1. Payroll employment indexed to 100 in November 2022, the month ChatGPT was released, for the
   information sector (CES5000000001, which includes software publishing and the big internet
   platforms), computer systems design and related services (CES6054150001), finance and insurance
   (CES5552000001) and all nonfarm jobs (CES0000000001).
2. Unemployment rates as 12 month averages: people aged 20 to 24 (LNS14000036), everyone
   (LNS14000000) and graduates aged 25 and over (LNS14027662), and the gap between the young and
   everyone.
3. Job openings in the information sector (JTS510000000000000JOL), 12 month average.
"""
from common import *

style(); b = bls()
start = "2022-11-01"
emp = b[["CES5000000001", "CES6054150001", "CES5552000001", "CES0000000001"]].loc["2019-01-01":]
idx = emp.div(emp.loc[start]) * 100
ur = b[["LNS14000036", "LNS14000000", "LNS14027662"]].astype(float).interpolate().rolling(12).mean()
jol = b["JTS510000000000000JOL"].rolling(12).mean()
last = emp.dropna().index[-1]
res = pd.Series({"info_change_since_nov22_k": emp.loc[last, "CES5000000001"] - emp.loc[start, "CES5000000001"],
                 "info_change_since_nov22_pct": idx.loc[last, "CES5000000001"] - 100,
                 "info_peak_k": emp.CES5000000001.max(), "info_peak_month": emp.CES5000000001.idxmax().strftime("%Y-%m"),
                 "csd_change_pct": idx.loc[last, "CES6054150001"] - 100, "fin_change_pct": idx.loc[last, "CES5552000001"] - 100,
                 "nonfarm_change_pct": idx.loc[last, "CES0000000001"] - 100,
                 "ur_20_24_12m_now": ur.LNS14000036.iloc[-1], "ur_all_12m_now": ur.LNS14000000.iloc[-1], "ur_grads_12m_now": ur.LNS14027662.iloc[-1],
                 "ur_20_24_12m_2022": ur.LNS14000036.loc["2022-11-01"], "ur_grads_12m_2022": ur.LNS14027662.loc["2022-11-01"],
                 "info_openings_12m_now_k": jol.dropna().iloc[-1], "info_openings_12m_2022_peak_k": jol.loc["2022-01-01":"2022-12-01"].max()})
save_table(res.to_frame("value"), "m08_summary"); save_table(idx.round(1), "m08_employment_index")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
for c, col, lab in (("CES0000000001", GREY, "All US jobs"), ("CES5552000001", VIOLET, "Finance and insurance"),
                    ("CES6054150001", ORANGE, "Computer systems design"), ("CES5000000001", BLUE, "Information sector")):
    s = idx[c].loc["2022-01-01":]
    ax.plot(s.index, s.values, color=col, lw=2 if c == "CES5000000001" else 1.5, label=lab)
    ax.text(s.index[-1] + pd.Timedelta(days=25), s.iloc[-1], f"{s.iloc[-1] - 100:+.1f}%", va="center", fontsize=8, color=col)
ax.axvline(pd.Timestamp(start), color=INK2, ls=":", lw=1); ax.text(pd.Timestamp(start) + pd.Timedelta(days=20), 89.5, "ChatGPT\nreleased", fontsize=7.5, color=INK2, va="top")
ax.axhline(100, color=INK2, lw=0.6); ax.set_xlim(pd.Timestamp("2022-01-01"), pd.Timestamp("2027-04-01")); ax.set_ylim(86, 112)
ax.set_ylabel("Payroll jobs, Nov 2022 = 100"); ax.legend(fontsize=7.2, loc="upper center", ncol=2)
ax.set_title("Tech jobs have been falling for four years", fontsize=10.5)
ax = axes[1]
for c, col, lab in (("LNS14000036", RED, "Aged 20 to 24"), ("LNS14000000", GREY, "Everyone"), ("LNS14027662", GREEN, "Graduates aged 25 and over")):
    s = ur[c].loc["2021-06-01":]
    ax.plot(s.index, s.values, color=col, label=lab)
    ax.text(s.index[-1] + pd.Timedelta(days=25), s.iloc[-1], f"{s.iloc[-1]:.1f}%", va="center", fontsize=8, color=col)
ax.axvline(pd.Timestamp(start), color=INK2, ls=":", lw=1)
ax.set_xlim(pd.Timestamp("2021-06-01"), pd.Timestamp("2027-04-01")); ax.set_ylim(0, 12); ax.set_ylabel("Unemployment rate, 12 month average, %")
ax.legend(fontsize=7.5, loc="upper right"); ax.set_title("The young are squeezed, not wiped out", fontsize=10.5)
finish(fig, "Figure 8: The official data shows a slow squeeze, not an AI jobs collapse",
       "author's model 08; US Bureau of Labor Statistics (CES, CPS and JOLTS) via the BLS public API, to September 2026.", "fig08_labour_market.png")
print(res)
