"""
MODEL 03  How long does Meta's new money last?
Meta has not guided 2027 capex. This grid asks what its 2027 free cash flow would be for a range of
capex growth rates (0% to 50% on the $140bn midpoint for 2026) and operating cash flow growth rates
(5% to 30% on the 2026 estimate from model 02), and subtracts the payments still owed under the
August 2026 settlement with state attorneys general (up to $18.59bn in total, of which the $9.89bn
charge was booked in 2026; the model assumes the full $18.59bn is paid during 2027 as a cautious case).
The result is compared with the $37.5bn of equity launched in October 2026. A cell below minus
$37.5bn means the launched equity would not cover 2027 alone and Meta would need the $60bn at the
market programme or more debt.
"""
from common import *

style(); h = hand()
base = pd.read_csv(ROOT / "04 Outputs" / "tables" / "m02_meta_cash.csv", index_col=0)
ocf26, capex26 = base.loc[2026, "ocf"], base.loc[2026, "capex"]
cg = np.array([0, 10, 20, 30, 40, 50]); og = np.array([5, 10, 15, 20, 25, 30])
legal = h["meta_legal_settlement_max"]
grid = pd.DataFrame([[ocf26 * (1 + o / 100) - capex26 * (1 + c / 100) - legal for c in cg] for o in og],
                    index=[f"{o}%" for o in og], columns=[f"{c}%" for c in cg])
eq = h["meta_common_offering_usd_bn"] + h["meta_preferred_usd_bn"]
share_exhausted = (grid < -eq).values.mean() * 100
res = pd.Series({"ocf_2026e": ocf26, "capex_2026": capex26, "legal_assumed_2027": legal, "equity_launched": eq,
                 "fcf_2027_flat_capex_15pct_ocf": grid.loc["15%", "0%"], "fcf_2027_capex_30_ocf_15": grid.loc["15%", "30%"],
                 "share_of_cells_beyond_launched_equity_pct": share_exhausted})
save_table(grid.round(1), "m03_fcf_2027_grid"); save_table(res.round(2).to_frame("value"), "m03_summary")

fig, ax = plt.subplots(figsize=(8.6, 4.6))
from matplotlib.colors import TwoSlopeNorm
im = ax.imshow(grid.values, cmap="RdYlGn", norm=TwoSlopeNorm(vmin=-90, vcenter=0, vmax=60), aspect="auto", origin="lower")
for i in range(len(og)):
    for j in range(len(cg)):
        v = grid.values[i, j]
        ax.text(j, i, f"{v:+.0f}", ha="center", va="center", fontsize=9, color="white" if v < -55 else INK, fontweight="bold" if v < -eq else "normal")
ax.set_xticks(range(len(cg))); ax.set_xticklabels(grid.columns); ax.set_yticks(range(len(og))); ax.set_yticklabels(grid.index)
ax.set_xlabel("Growth in capital spending in 2027"); ax.set_ylabel("Growth in cash from operations in 2027"); ax.grid(False)
cb = fig.colorbar(im, ax=ax, shrink=0.85); cb.set_label("2027 free cash flow after settlement, US$ bn", fontsize=8)
ax.set_title("Bold numbers need more than the $37.5bn already raised", fontsize=10.5)
finish(fig, "Figure 3: If capex keeps growing, Meta will need the rest of its $97.5bn plan",
       "author's model 03; built on model 02's 2026 estimate; Meta Q3 2026 results (settlement terms).", "fig03_meta_2027.png")
print(grid.round(0)); print(res.round(2))
