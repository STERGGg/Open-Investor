"""
MODEL 09  How much can Trump hurt Brazil?
1. Brazil's goods exports by destination, 2015 to 2025, from the IMF's International Trade in
   Goods by partner country (IMTS) via OpenBB, as a share of total exports.
2. Exports to the US as a share of GDP in 2025: exports in dollars converted at the 2025
   average real per dollar (Banco Central do Brasil series 3698) and divided by the IMF's 2025
   nominal GDP in reais. This is the most that a US tariff could touch, before exemptions.
3. US tariffs on Brazil: 10% base from April 2025, 50% from 30 July 2025 with exemptions, and
   25% on certain goods under Section 301 from July 2026.
"""
from common import *

style(); h = hand()
ex = pd.read_csv(DATA / "imf_imts_brazil_exports_usd_bn.csv", index_col=0)
share = ex.drop(columns="World").div(ex.World, axis=0) * 100
fx25 = bcb().brl_per_usd.loc["2025"].mean()
ngdp25 = pd.read_csv(DATA / "imf_weo_bra_nominal.csv", index_col=0).nominal_gdp_brl_bn.loc[2025]
us_gdp = ex.loc[2025, "United States"] * fx25 / ngdp25 * 100
res = pd.Series({"us_share_2025": share.loc[2025, "United States"], "china_share_2025": share.loc[2025, "China"],
                 "eu_share_2025": share.loc[2025, "European Union"], "us_exports_usd_bn_2025": ex.loc[2025, "United States"],
                 "us_exports_pct_gdp_2025": us_gdp, "china_to_us_ratio": ex.loc[2025, "China"] / ex.loc[2025, "United States"],
                 "us_exports_change_2024_25_pct": (ex.loc[2025, "United States"] / ex.loc[2024, "United States"] - 1) * 100})
save_table(share.round(1), "m09_export_shares"); save_table(res.round(2).to_frame("value"), "m09_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.4, 1]})
ax = axes[0]
for c, col in (("China", RED), ("European Union", BLUE), ("United States", ORANGE), ("Argentina", GREY)):
    ax.plot(share.index, share[c], color=col, marker="o", ms=3, label=c)
    ax.text(2025.2, share.loc[2025, c], f"{share.loc[2025, c]:.0f}%", va="center", fontsize=8.5, color=col)
ax.set_xlim(2014.5, 2026.3); ax.set_ylabel("% of Brazil's goods exports"); ax.legend(fontsize=8, loc="upper left")
ax.set_title("China buys almost three times as much as the US", fontsize=10.5)
ax = axes[1]
labs = ["April 2025\nbase tariff", "July 2025\n(with exemptions)", "July 2026\nSection 301"]
vals = [10, h["us_tariff_2025"], h["us_tariff_301"]]
ax.bar(range(3), vals, color=[GREY, RED, ORANGE], width=0.55)
for i, v in enumerate(vals):
    ax.text(i, v + 1.2, f"{v:.0f}%", ha="center", fontsize=9)
ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=8); ax.set_ylim(0, 60); ax.set_ylabel("US tariff on Brazilian goods, %")
ax.grid(axis="x", visible=False); ax.set_title("Trump's tariffs on Brazil", fontsize=10.5)
finish(fig, "Figure 9: The US matters to Brazil, but China matters more",
       "author's model 09; IMF IMTS via OpenBB; Banco Central do Brasil; USTR (Jul 2026); Wikipedia (2025 and 2026 dispute).", "fig09_trade.png")
print(share.round(1).tail(4)); print(res.round(2))
