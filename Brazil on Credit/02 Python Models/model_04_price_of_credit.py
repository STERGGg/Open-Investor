"""
MODEL 04  What credit costs, and what happens to a R$100 food shop
1. Average annual interest rates on household credit in August 2026 from the Banco Central do
   Brasil (SGS): revolving credit card (22022), card instalment plans (22023), overdraft (20741),
   personal loans not tied to payroll (20742), payroll deducted loans (20747), all household
   free resource credit (20740) and the Selic (4189).
2. A R$100 supermarket bill left on the revolving card: the annual rate converted to a monthly
   rate, (1 + r) ** (1/12) - 1, and compounded for 12 months, with and without the legal cap that
   since January 2024 limits interest and charges on revolving card debt to 100% of the original
   amount. The comparison uses a payroll loan and the same bill paid in a normal card instalment
   plan, which charges the shopper no interest when the shop offers interest free instalments.
3. Share of revolving card debt that is more than 90 days late (21127).
"""
from common import *

style(); h = hand()
b = bcb().loc["2026-08-01"]
rates = pd.Series({"Revolving credit card": b.rate_card_revolving_pct, "Card instalment loan": b.rate_card_instalment_pct,
                   "Overdraft": b.rate_overdraft_pct, "Personal loan": b.rate_personal_nonpayroll_pct,
                   "All household credit": b.rate_pf_free_total_pct, "Payroll loan": b.rate_payroll_loan_pct,
                   "Selic (central bank)": bcb().selic_pct.dropna().iloc[-1]})
monthly = (1 + rates["Revolving credit card"] / 100) ** (1 / 12) - 1
months = np.arange(0, 13)
uncapped = 100 * (1 + monthly) ** months
capped = np.minimum(uncapped, 100 * (1 + h["revolving_cap"] / 100))
payroll = 100 * (1 + rates["Payroll loan"] / 100) ** (months / 12)
res = pd.Series({"revolving_monthly_pct": monthly * 100, "r100_after_12m_uncapped": uncapped[-1], "r100_after_12m_capped": capped[-1],
                 "months_to_hit_cap": int(np.argmax(uncapped >= 200)), "revolving_npl_pct": b.npl_card_revolving_pct,
                 "revolving_vs_selic_x": rates["Revolving credit card"] / rates["Selic (central bank)"]})
save_table(rates.round(2).to_frame("annual_rate_pct"), "m04_rates"); save_table(res.round(2).to_frame("value"), "m04_grocery")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.1, 1]})
ax = axes[0]
ax.barh(rates.index[::-1], rates.values[::-1], color=[GREY if "Selic" in k else (RED if "Revolving" in k else ORANGE) for k in rates.index[::-1]])
for i, v in enumerate(rates.values[::-1]):
    ax.text(v + 6, i, f"{v:.0f}%", va="center", fontsize=8.5)
ax.set_xlim(0, 520); ax.set_xlabel("Average interest rate, % a year (Aug 2026)"); ax.grid(axis="y", visible=False)
ax.tick_params(axis="y", labelsize=8.5); ax.set_title("The price of borrowing", fontsize=11)
ax = axes[1]
ax.plot(months, uncapped, color=RED, ls="--", label="Revolving card, if there were no cap")
ax.plot(months, capped, color=RED, label="Revolving card, with the 100% cap")
ax.plot(months, payroll, color=BLUE, label="Payroll loan")
ax.axhline(100, color=GREY, lw=1); ax.text(6.5, 80, "The R$100 food shop", fontsize=8, color=INK2); ax.set_ylim(60, 590)
ax.text(12.1, uncapped[-1], f"R${uncapped[-1]:.0f}", fontsize=8.5, color=RED, va="center")
ax.text(12.1, capped[-1], f"R${capped[-1]:.0f}", fontsize=8.5, color=RED, va="center")
ax.text(12.1, payroll[-1], f"R${payroll[-1]:.0f}", fontsize=8.5, color=BLUE, va="center")
ax.set_xlim(0, 13.5); ax.set_xticks(range(0, 13, 2)); ax.set_xlabel("Months"); ax.set_ylabel("What you owe, R$")
ax.legend(fontsize=7.5, loc="upper left"); ax.set_title("R$100 of groceries left on the card", fontsize=11)
finish(fig, "Figure 4: Credit cards cost 33 times the central bank rate",
       "author's model 04; Banco Central do Brasil SGS (Aug 2026); revolving cap under Law 14,690 (Monitor Mercantil).", "fig04_price_of_credit.png")
print(rates.round(1)); print(res.round(2))
