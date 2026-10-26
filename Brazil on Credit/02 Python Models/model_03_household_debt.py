"""
MODEL 03  How indebted are Brazilian households?
Banco Central do Brasil SGS monthly series since 2011:
1. Household debt with the financial system as % of the last 12 months' income (29037), and the
   same excluding mortgages (29038).
2. Debt service: the share of monthly income going on interest and repayments (29034).
3. Delinquency: share of household loans from free resources more than 90 days late (21112),
   and the Selic rate (4189) for context.
Records are the maximum since each series began.
"""
from common import *

style(); h = hand()
b = bcb()
cols = ["debt_pct_income", "debt_ex_housing_pct_income", "debt_service_pct_income", "npl_pf_free_pct", "selic_pct"]
latest = {c: (b[c].dropna().index[-1].strftime("%b %Y"), b[c].dropna().iloc[-1], b[c].max(), b[c].idxmax().strftime("%b %Y")) for c in cols}
t = pd.DataFrame(latest, index=["latest_month", "latest", "record", "record_month"]).T
save_table(t, "m03_household_debt")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
ax.plot(b.index, b.debt_pct_income, color=BLUE, label="All household debt, % of yearly income")
ax.plot(b.index, b.debt_service_pct_income, color=RED, label="Debt service, % of monthly income")
ax.plot(b.index, b.debt_ex_housing_pct_income, color=BLUE, ls=":", label="Debt excluding mortgages")
for c, col in (("debt_service_pct_income", RED),):
    s = b[c].dropna(); ax.annotate(f"{s.iloc[-1]:.1f}%, a record", (s.index[-1], s.iloc[-1]), (s.index[-1] - pd.Timedelta(days=1500), s.iloc[-1] + 6),
                                   fontsize=8, color=col, arrowprops=dict(arrowstyle="-", color=col, lw=0.8))
ax.set_ylim(15, 60); ax.set_ylabel("%"); ax.legend(fontsize=7.5, loc="upper left")
ax.set_title("Debt has stopped falling, the bill keeps rising", fontsize=10.5)
ax = axes[1]
ax.plot(b.index, b.npl_pf_free_pct, color=ORANGE, label="Household loans over 90 days late, %")
ax2 = ax.twinx(); ax2.plot(b.index, b.selic_pct, color=GREY, lw=1.3, label="Selic rate, % (right)")
ax2.spines["right"].set_visible(True); ax2.grid(False); ax2.set_ylim(0, 16)
s = b.npl_pf_free_pct.dropna()
ax.annotate(f"{s.iloc[-1]:.1f}%, highest\nsince the data began", (s.index[-1], s.iloc[-1]), (s.index[-1] - pd.Timedelta(days=1700), s.iloc[-1] + 0.3),
            fontsize=8, color=ORANGE, arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))
ax.set_ylim(3.5, 9); ax.set_ylabel("% of loans"); ax2.set_ylabel("Selic, %")
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels(); ax.legend(h1 + h2, l1 + l2, fontsize=7.5, loc="lower left")
ax.set_title("Defaults at a record, with rates at 14%", fontsize=10.5)
finish(fig, "Figure 3: Brazilian households are paying more of their income to the banks than ever",
       "author's model 03; Banco Central do Brasil SGS series 29037, 29038, 29034, 21112 and 4189 (to Aug 2026).", "fig03_household_debt.png")
print(t)
