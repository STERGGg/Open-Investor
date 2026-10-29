"""
MODEL 07  How much of the firing is really AI?
1. US job cuts announced each month, January to September, in 2025 and 2026, from the
   Challenger, Gray and Christmas report for September 2026 (03 Data/challenger_monthly.csv).
2. The share of announced cuts that employers attributed to artificial intelligence: about 55,000
   of roughly 1.2 million in 2025 (about 4.5%, as reported by IBTimes citing Challenger), against
   120,136 of 573,195 from January to September 2026.
3. Change from the same nine months of 2025 in total cuts, technology sector cuts, financial sector
   cuts and announced hiring plans.
Announced cuts are plans, not people actually let go, and the reason is whatever the employer chose
to give, so the AI share measures what companies say as much as what AI does.
"""
from common import *

style(); h = hand()
ch = pd.read_csv(DATA / "challenger_monthly.csv", index_col=0)
ai_share_26 = h["chal_ytd26_ai"] / h["chal_ytd26_total"] * 100
ai_share_25 = h["chal_2025_ai_share"]
chg = pd.Series({"All announced cuts": (h["chal_ytd26_total"] / h["chal_ytd25_total"] - 1) * 100,
                 "Technology sector cuts": (h["chal_ytd26_tech"] / h["chal_ytd25_tech"] - 1) * 100,
                 "Financial sector cuts": (h["chal_ytd26_fin"] / h["chal_ytd25_fin"] - 1) * 100})
non_ai_26 = h["chal_ytd26_total"] - h["chal_ytd26_ai"]
res = pd.Series({"ytd26_total": h["chal_ytd26_total"], "ytd25_total": h["chal_ytd25_total"], "ytd26_ai": h["chal_ytd26_ai"], "ai_share_26_pct": ai_share_26,
                 "ai_share_25_pct": ai_share_25, "non_ai_cuts_26": non_ai_26, "non_ai_change_vs_25_total_pct": (non_ai_26 / h["chal_ytd25_total"] - 1) * 100,
                 "sep26_ai": h["chal_sep26_ai"], "sep26_ai_share_pct": h["chal_sep26_ai"] / ch.loc["Sep", "cuts_2026"] * 100}
                | {f"chg_{k}": v for k, v in chg.items()})
save_table(res.round(2).to_frame("value"), "m07_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.4, 1]})
ax = axes[0]
x = np.arange(len(ch))
ax.bar(x - 0.2, ch.cuts_2025 / 1000, 0.4, color=GREY, label="2025")
ax.bar(x + 0.2, ch.cuts_2026 / 1000, 0.4, color=BLUE, label="2026")
ax.set_xticks(x); ax.set_xticklabels(ch.index); ax.set_ylabel("US job cuts announced, thousand"); ax.legend(fontsize=8, loc="upper right")
ax.text(0.03, 0.95, f"January to September\n2025: {h['chal_ytd25_total'] / 1000:,.0f}k\n2026: {h['chal_ytd26_total'] / 1000:,.0f}k ({chg.iloc[0]:+.0f}%)", transform=ax.transAxes,
        fontsize=8, va="top", color=INK2)
ax.grid(axis="x", visible=False); ax.set_title("Fewer cuts overall this year", fontsize=10.5)
ax = axes[1]
labs = ["2025\n(full year)", "2026\n(Jan to Sep)"]
ax.bar([0, 1], [ai_share_25, ai_share_26], color=[GREY, RED], width=0.5)
for j, v in enumerate([ai_share_25, ai_share_26]):
    ax.text(j, v + 0.6, f"{v:.1f}%", ha="center", fontsize=9)
ax.text(1, ai_share_26 / 2, f"{h['chal_ytd26_ai'] / 1000:.0f}k\njobs", ha="center", color="white", fontsize=8.5, fontweight="bold")
ax.set_xticks([0, 1]); ax.set_xticklabels(labs); ax.set_ylim(0, 27); ax.set_ylabel("% of announced cuts blamed on AI"); ax.grid(axis="x", visible=False)
ax.text(0.5, 24.5, f"Tech sector cuts {chg.iloc[1]:+.0f}%, finance {chg.iloc[2]:+.0f}%", ha="center", fontsize=8, color=INK2)
ax.set_title("But AI is now the top excuse", fontsize=10.5)
finish(fig, "Figure 7: Companies are firing less in total, and blaming AI far more",
       "author's model 07; Challenger, Gray and Christmas job cut report for September 2026; IBTimes (Sep 2026) for the 2025 AI share.", "fig07_ai_blame.png")
print(res.round(2))
