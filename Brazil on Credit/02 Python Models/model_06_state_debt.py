"""
MODEL 06  The government's own debt
1. Gross general government debt as % of GDP, monthly from the Banco Central do Brasil (13762,
   the Brazilian definition) since 2011, and the IMF's projection on its own wider definition to
   2031 (WEO October 2026, GGXWDG_NGDP). The two definitions differ, so they are shown as
   separate lines.
2. Interest bill: the IMF's overall deficit minus its primary balance, both as % of GDP. This is
   what the government pays in interest each year, which is what keeps the deficit large even
   though the primary balance is close to zero.
3. Debt stabilising primary balance in 2027: d x (r - g) / (1 + g), with d the IMF's 2026 debt,
   r the implied average interest rate (2026 interest / 2025 debt) and g nominal GDP growth from
   the IMF's 2027 real growth plus 4.25% inflation (the Focus survey's 2027 expectation via The
   Rio Times, Aug 2026).
"""
from common import *

style(); h = hand()
b = bcb(); imf_debt = weo("ggxwdg"); overall = weo("ggxcnl"); primary = weo("ggxonlb"); gdp = weo("gdp")
interest = (primary - overall).dropna()
d26 = imf_debt.loc[2026] / 100; r = interest.loc[2026] / imf_debt.loc[2025]
g = (1 + gdp.loc[2027] / 100) * 1.0425 - 1
stab = d26 * (r - g) / (1 + g) * 100
res = pd.Series({"bcb_gross_debt_latest": b.gross_gov_debt_pct_gdp.dropna().iloc[-1], "bcb_gross_debt_low": b.gross_gov_debt_pct_gdp.loc["2021":].min(),
                 "imf_debt_2026": imf_debt.loc[2026], "imf_debt_2031": imf_debt.loc[2031], "interest_2026_pct_gdp": interest.loc[2026],
                 "primary_2026_pct_gdp": primary.loc[2026], "implied_interest_rate_pct": r * 100, "nominal_growth_2027_pct": g * 100,
                 "debt_stabilising_primary_pct_gdp": stab, "budget_target_2027": h["budget_2027_primary_target"]})
save_table(res.round(2).to_frame("value"), "m06_state_debt"); save_table(pd.DataFrame({"interest": interest, "primary": primary}).round(2), "m06_interest")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
ax.plot(b.index, b.gross_gov_debt_pct_gdp, color=BLUE, label="Gross debt, Brazilian definition (BCB)")
yrs = pd.to_datetime([f"{y}-12-31" for y in imf_debt.index])
ax.plot(yrs, imf_debt.values, color=ORANGE, ls="--", marker="o", ms=3, label="IMF definition, with forecast to 2031")
ax.axvspan(pd.Timestamp("2026-10-01"), pd.Timestamp("2031-12-31"), color=GREY, alpha=0.12)
ax.text(pd.Timestamp("2027-03-01"), 58, "IMF\nforecast", fontsize=8, color=INK2)
ax.set_ylabel("% of GDP"); ax.set_ylim(50, 110); ax.legend(fontsize=7.5, loc="upper left")
ax.set_title("Public debt is climbing again", fontsize=11)
ax = axes[1]
yy = interest.loc[2015:2031]
ax.bar(yy.index - 0.2, yy.values, 0.4, color=RED, label="Interest paid")
ax.bar(primary.loc[2015:2031].index + 0.2, -primary.loc[2015:2031].values, 0.4, color=GREY, label="Primary deficit (minus = surplus)")
ax.axhline(0, color=INK2, lw=0.8); ax.axvline(2026.5, color=INK2, ls=":", lw=1)
ax.set_ylabel("% of GDP"); ax.legend(fontsize=7.5, loc="upper right"); ax.grid(axis="x", visible=False); ax.set_xticks(range(2015, 2032, 2)); ax.tick_params(axis="x", labelsize=8); ax.set_ylim(-3, 10.5)
ax.set_title("Almost the whole deficit is interest", fontsize=11)
finish(fig, "Figure 6: The state borrows at the same high rates as everyone else",
       "author's model 06; Banco Central do Brasil SGS 13762; IMF World Economic Outlook (Oct 2026).", "fig06_state_debt.png")
print(res.round(2)); print(interest.round(2))
