"""
MODEL 02  Why Meta is selling shares
1. Meta's operating cash flow against its capital expenditure, 2022 to 2025 from the annual cash
   flow statements (Nasdaq via OpenBB), and 2026 built from the first three quarters plus an
   estimate for the fourth. Fourth quarter operating cash flow is assumed equal to the average of
   the first three quarters of 2026 scaled up by Meta's guided fourth quarter revenue growth over
   the third quarter (midpoint of $73bn to $76bn against $64.6bn). Fourth quarter capex is the
   midpoint of the $135bn to $145bn full year guidance minus the first three quarters, using
   Meta's own figures including finance lease payments (the 2022 to 2025 bars exclude them, so
   they understate capex slightly).
2. The swing in Meta's capital return. Net stock issuance from the cash flow statement (negative
   means buybacks) for 2022 to 2025, against the equity launched on 26 October 2026: $25bn of
   common stock sold forward at $625 and $12.5bn of mandatory convertible preferred, plus a
   $60bn at the market programme that has not started.
3. Dilution: shares to be issued by the common offering, and the whole $97.5bn programme if it
   were all sold at $625, as a share of the 2.56bn shares outstanding. The preferred converts later
   at a price not yet known, so it is counted at $625 as an approximation.
"""
from common import *

style(); h = hand()
c = fundamentals("cash_flow"); i = fundamentals("income")
m = c[(c.symbol == "META") & (c.fiscal_period == "annual")]; m = m.set_index(m.period_ending.dt.year)
mq = c[(c.symbol == "META") & (c.fiscal_period == "quarter")].set_index("period_ending")
iq = i[(i.symbol == "META") & (i.fiscal_period == "quarter")].set_index("period_ending")
ocf = (m.net_cash_flow_from_operating_activities / 1e6).astype(float)
capex = (-m.capital_expenditure / 1e6).astype(float)
q26 = mq.loc["2026-01-01":]
ocf_9m = q26.net_cash_flow_from_operating_activities.sum() / 1e6
rev_q3 = iq.loc["2026-09-30", "revenue"] / 1e6
q4_growth = (h["meta_q4_rev_mid"] / rev_q3)
ocf_q4 = ocf_9m / 3 * q4_growth
capex_mid = (h["meta_capex_2026_low"] + h["meta_capex_2026_high"]) / 2
ocf[2026] = ocf_9m + ocf_q4; capex[2026] = capex_mid
fcf = ocf - capex
issu = (m.net_stock_issuance / 1e6).astype(float)
eq_now = h["meta_common_offering_usd_bn"] + h["meta_preferred_usd_bn"]
programme = eq_now + h["meta_atm_usd_bn"]
sh_common = h["meta_common_offering_usd_bn"] / h["meta_common_price"]
dil_common = sh_common / h["meta_shares_out_bn"] * 100
dil_all = programme / h["meta_common_price"] / h["meta_shares_out_bn"] * 100
res = pd.Series({"ocf_2025": ocf[2025], "capex_2025": capex[2025], "fcf_2025": fcf[2025], "ocf_2026e": ocf[2026], "capex_2026_mid": capex[2026],
                 "fcf_2026e": fcf[2026], "capex_to_ocf_2026e_pct": capex[2026] / ocf[2026] * 100, "capex_to_ocf_2022_pct": capex[2022] / ocf[2022] * 100,
                 "buybacks_2024": -issu[2024], "buybacks_2025": -issu[2025], "equity_launched": eq_now, "equity_programme": programme,
                 "swing_vs_2024": eq_now + (-issu[2024]), "new_common_shares_m": sh_common * 1000, "dilution_common_pct": dil_common, "dilution_all_pct": dil_all,
                 "ltdebt_increase_2026": h["meta_ltdebt_q3_26"] - h["meta_ltdebt_dec25"], "legal_settlement_max": h["meta_legal_settlement_max"]})
save_table(pd.DataFrame({"ocf": ocf, "capex": capex, "fcf": fcf, "net_stock_issuance": issu}).round(1), "m02_meta_cash"); save_table(res.round(2).to_frame("value"), "m02_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.35, 1]})
ax = axes[0]
yrs = list(ocf.index); x = np.arange(len(yrs))
ax.bar(x - 0.2, ocf.values, 0.4, color=BLUE, label="Cash from operations")
ax.bar(x + 0.2, capex.values, 0.4, color=ORANGE, label="Capital expenditure")
ax.plot(x, fcf.values, color=INK, marker="o", lw=1.6, label="Free cash flow")
for j, v in enumerate(fcf.values):
    ax.text(j + 0.08, v - 10 if v < 5 else v + 5, f"{v:+.0f}", ha="left", fontsize=8.5, fontweight="bold")
ax.axhline(0, color=INK2, lw=0.8)
ax.set_xticks(x); ax.set_xticklabels([str(y) if y < 2026 else "2026\n(estimate)" for y in yrs]); ax.set_ylabel("US$ billion"); ax.set_ylim(-25, 160)
ax.legend(fontsize=8, loc="upper left"); ax.grid(axis="x", visible=False)
ax.set_title("The data centres now eat all the cash", fontsize=10.5)
ax = axes[1]
lab = ["2022", "2023", "2024", "2025", "Oct 2026\nlaunched", "Oct 2026\nwhole plan"]
vals = list(issu.loc[2022:2025].values) + [eq_now, programme]
ax.bar(range(len(vals)), vals, color=[GREEN] * 4 + [RED, "#f0a3a2"], width=0.6)
for j, v in enumerate(vals):
    ax.text(j, v + (3 if v > 0 else -7), f"{v:+.0f}", ha="center", fontsize=8.5)
ax.axhline(0, color=INK2, lw=0.8); ax.set_xticks(range(len(vals))); ax.set_xticklabels(lab, fontsize=7.8)
ax.set_ylabel("US$ billion (minus = buying back shares)"); ax.set_ylim(-40, 110); ax.grid(axis="x", visible=False)
ax.set_title("From buying back shares to selling them", fontsize=10.5)
finish(fig, "Figure 2: Meta is raising equity because its AI bill outgrew its cash",
       "author's model 02; Meta cash flow statements (Nasdaq via OpenBB); Meta Q3 2026 results and guidance; FinanceFeeds and Rallies (offering terms).", "fig02_meta_cash.png")
print(pd.DataFrame({"ocf": ocf, "capex": capex, "fcf": fcf}).round(1)); print(res.round(2))
