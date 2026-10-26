"""
MODEL 05  Who is in debt, and what the election promises cost
1. CNC Peic survey (July 2026): share of families in debt and in arrears for those earning up to
   three minimum wages and above ten, and which kinds of debt families report (more than one
   allowed, so shares add to more than 100%).
2. The pre election measures and their scale in R$ billion: Desenrola 3.0's expected cost (R$15bn
   at a 90% discount on R$150bn of face value), the 15% Bolsa Familia rise (R$22bn), tax lost
   from the betting ban (R$5.3bn), household net losses to online betting in 2025 (R$62bn), and
   overdue household debts on record with Serasa (R$586.4bn, July 2026).
"""
from common import *

style(); h = hand()
inc = pd.DataFrame({"In debt": [h["cnc_low_in_debt"], h["cnc_high_in_debt"]], "Behind on payments": [h["cnc_low_arrears"], h["cnc_high_arrears"]]},
                   index=["Up to 3 minimum wages\n(about R$4,860 a month)", "Over 10 minimum wages"])
kinds = pd.Series({"Credit card": h["cnc_card_share"], "Store instalments": h["cnc_store_share"], "Personal loan": h["cnc_personal_share"], "Car finance": h["cnc_car_share"]})
money = pd.Series({"Overdue debts\n(Serasa)": h["serasa_overdue_brl_bn"], "Lost to online\nbetting, 2025": h["bets_losses_2025"],
                   "Bolsa Família\nrise": h["bolsa_rise_cost"], "Desenrola 3.0\ndebt buyout": h["desenrola3_cost"], "Tax lost from\nbetting ban": h["bet_ban_tax_loss"]})
save_table(inc, "m05_by_income"); save_table(kinds.to_frame("pct_of_indebted_families"), "m05_kinds"); save_table(money.to_frame("brl_bn"), "m05_money")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1, 1.25]})
ax = axes[0]
x = np.arange(2)
ax.bar(x - 0.18, inc["In debt"], 0.36, color=BLUE, label="In debt")
ax.bar(x + 0.18, inc["Behind on payments"], 0.36, color=RED, label="Behind on payments")
for i in range(2):
    ax.text(i - 0.18, inc["In debt"].iloc[i] + 1.5, f"{inc['In debt'].iloc[i]:.1f}%", ha="center", fontsize=8.5)
    ax.text(i + 0.18, inc["Behind on payments"].iloc[i] + 1.5, f"{inc['Behind on payments'].iloc[i]:.1f}%", ha="center", fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(inc.index, fontsize=8); ax.set_ylim(0, 102); ax.set_ylabel("% of families")
ax.legend(fontsize=8, loc="upper right", bbox_to_anchor=(1, 0.9)); ax.grid(axis="x", visible=False)
ax.text(0.5, 96, f"Of families in debt, {kinds['Credit card']:.0f}% owe on a credit card", ha="center", fontsize=8, color=INK2)
ax.set_title("The poorest are most in debt, and most behind", fontsize=10.5)
ax = axes[1]
ax.barh(money.index[::-1], money.values[::-1], color=[RED, ORANGE, GREEN, GREEN, GREY][::-1])
for i, v in enumerate(money.values[::-1]):
    ax.text(v + 6, i, f"R${v:,.0f}bn" if v >= 10 else f"R${v:.1f}bn", va="center", fontsize=8.5)
ax.set_xlim(0, 680); ax.set_xlabel("R$ billion"); ax.tick_params(axis="y", labelsize=8); ax.grid(axis="y", visible=False)
ax.set_title("The size of the hole and the size of the fix", fontsize=10.5)
finish(fig, "Figure 5: Who owes, and what the election promises cost",
       "author's model 05; CNC Peic (Jul 2026) and Serasa via The Rio Times; Agência Brasil (betting losses).", "fig05_relief.png")
print(inc); print(kinds); print(money)
