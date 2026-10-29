"""
MODEL 04  Do the job cuts pay for the AI?
1. Capital expenditure per employee. Meta: calendar year capex from the cash flow statement (2026 at
   the midpoint of guidance) divided by the latest reported headcount in that year (Q3 for 2025 and
   2026, year end otherwise). Microsoft: fiscal year capex (to June) divided by headcount at 30 June.
2. What the cuts save in a year, against what is being spent on AI.
   Meta: 8,000 jobs cut in May 2026 times the median employee's 2025 total pay of $388,200 (proxy
     statement). Median pay includes stock awards, so this is the cost the company stops incurring.
   Microsoft: 60,000 people eligible for the buyout times the 30% who took the earlier voluntary
     retirement offer, times the median pay of $200,972 (fiscal 2025 proxy). Microsoft itself expects
     lower take up, so this is generous.
   Barclays: 5,000 jobs times average compensation per full time employee in 2025 (£9,253m of
     compensation costs over 93,000 staff). Barclays has no AI capex line, so its saving is set
     against its own 2025 staff costs of £10,607m instead.
   Each saving is compared with the company's own spending base, and the sensitivity table shows the
   Meta and Microsoft figures if the people leaving earn 50% more or 50% less than the median.
"""
from common import *

style(); h = hand()
c = fundamentals("cash_flow")
mc = c[(c.symbol == "META") & (c.fiscal_period == "annual")]; mc = mc.set_index(mc.period_ending.dt.year)
sc = c[(c.symbol == "MSFT") & (c.fiscal_period == "annual")]; sc = sc.set_index(sc.period_ending.dt.year)
meta_capex = (-mc.capital_expenditure / 1e6).astype(float); meta_capex[2026] = (h["meta_capex_2026_low"] + h["meta_capex_2026_high"]) / 2
meta_hc = pd.Series({2022: h["meta_headcount_2022q4"], 2023: h["meta_headcount_2023q4"], 2024: h["meta_headcount_2024q4"], 2025: h["meta_headcount_2025q3"], 2026: h["meta_headcount_2026q3"]})
ms_capex = (-sc.capital_expenditure / 1e6).astype(float)
ms_hc = pd.Series({y: h[f"msft_headcount_{y}"] for y in ms_capex.index})
meta_cpe = meta_capex / meta_hc * 1e6   # US$ thousand per employee
ms_cpe = ms_capex / ms_hc * 1e6

meta_save = h["meta_cut_apr26"] * h["meta_median_pay_2025"] / 1e9
ms_save = h["msft_buyout_eligible"] * h["msft_prior_retirement_uptake"] * h["msft_median_pay_fy25"] / 1e9
bcs_avg = h["bcs_comp_costs_2025_gbp_m"] / h["bcs_fte_2025"] * 1e6
bcs_save = h["bcs_cuts_2026"] * bcs_avg / 1e6  # GBP m
pct = pd.Series({"Meta: pay saved as % of 2026 capex": meta_save / meta_capex[2026] * 100,
                 "Microsoft: pay saved as % of FY2026 capex": ms_save / ms_capex[2026] * 100,
                 "Barclays: pay saved as % of its staff costs": bcs_save / h["bcs_staff_costs_2025_gbp_m"] * 100})
sens = pd.DataFrame({m: {"meta_pct_of_capex": meta_save * m / meta_capex[2026] * 100, "msft_pct_of_capex": ms_save * m / ms_capex[2026] * 100} for m in (0.5, 1.0, 1.5)}).T
sens.index.name = "pay_multiple_of_median"
res = pd.Series({"meta_capex_per_emp_2022_k": meta_cpe[2022], "meta_capex_per_emp_2026_k": meta_cpe[2026], "ms_capex_per_emp_2023_k": ms_cpe[2023],
                 "ms_capex_per_emp_2026_k": ms_cpe[2026], "meta_saving_usd_bn": meta_save, "ms_saving_usd_bn": ms_save, "bcs_avg_comp_gbp": bcs_avg,
                 "bcs_saving_gbp_m": bcs_save, "bcs_struct_cost_actions_2026_gbp_m": h["bcs_struct_cost_2026_gbp_m"],
                 "meta_days_of_capex_saved": meta_save / meta_capex[2026] * 365, "ms_days_of_capex_saved": ms_save / ms_capex[2026] * 365}
                | {k: v for k, v in pct.items()})
save_table(pd.DataFrame({"meta_capex_per_employee_k": meta_cpe, "msft_capex_per_employee_k": ms_cpe}).round(0), "m04_capex_per_employee")
save_table(sens.round(2), "m04_sensitivity"); save_table(res.round(2).to_frame("value"), "m04_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw={"width_ratios": [1.1, 1.1]})
ax = axes[0]
ax.plot(meta_cpe.index, meta_cpe.values, color=BLUE, marker="o", label="Meta (calendar year)")
ax.plot(ms_cpe.index, ms_cpe.values, color=GREEN, marker="o", label="Microsoft (year to June)")
for s, col in ((meta_cpe, BLUE), (ms_cpe, GREEN)):
    for yy in (s.index[0], s.index[-1]):
        ax.text(yy, s[yy] + 70, f"${s[yy]:,.0f}k", ha="center", fontsize=8, color=col)
ax.set_ylabel("Capital spending per employee, US$ thousand"); ax.set_ylim(0, 2400); ax.legend(fontsize=8, loc="upper left")
ax.set_xticks(range(2022, 2027)); ax.set_xticklabels(["2022", "2023", "2024", "2025", "2026\n(estimate)"])
ax.set_title("Each worker now comes with $2m of data centre", fontsize=10.5)
ax = axes[1]
labs = ["Meta\n8,000 cut, % of 2026 capex", "Microsoft\nbuyouts, % of FY2026 capex", "Barclays\n5,000 cut, % of staff costs"]
ax.bar(range(3), pct.values, color=[BLUE, GREEN, VIOLET], width=0.55)
for j, v in enumerate(pct.values):
    ax.text(j, v + 0.15, f"{v:.1f}%", ha="center", fontsize=9)
ax.text(0, pct.iloc[0] + 0.9, f"${meta_save:.1f}bn a year", ha="center", fontsize=7.5, color=INK2)
ax.text(1, pct.iloc[1] + 0.9, f"${ms_save:.1f}bn a year", ha="center", fontsize=7.5, color=INK2)
ax.text(2, pct.iloc[2] + 0.9, f"£{bcs_save:.0f}m a year", ha="center", fontsize=7.5, color=INK2)
ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=7.8); ax.set_ylim(0, 7.5); ax.set_ylabel("Annual pay saved, %"); ax.grid(axis="x", visible=False)
ax.set_title("The cuts are small change next to the AI bill", fontsize=10.5)
finish(fig, "Figure 4: Firing people does not fund the data centres",
       "author's model 04; cash flow statements (Nasdaq via OpenBB); Meta and Microsoft proxy statements; Barclays 2025 Form 20-F; company announcements.", "fig04_people_vs_gpus.png")
print(pd.DataFrame({"meta": meta_cpe, "msft": ms_cpe}).round(0)); print(res.round(2)); print(sens.round(2))
