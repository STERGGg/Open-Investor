"""
MODEL 08  Can Lula afford his fourth term?
A Monte Carlo simulation of Brazil's gross public debt over the four years of the new term,
2027 to 2030, on the IMF's debt definition and October 2026 World Economic Outlook forecasts.

1. Debt engine: d(t) = d(t-1) x (1 + i) / (1 + n) - pb(t) + sfa(t), where i is the average
   interest rate on the debt (IMF interest bill divided by last year's debt), n is nominal GDP
   growth (IMF), pb is the primary balance (IMF) and sfa is a residual that makes the IMF
   baseline reproduce exactly. The residual is kept in every path.

2. Two policy scenarios, run on exactly the same random shocks so that they can be compared
   path by path:
   Promises: the IMF primary balance minus the unbudgeted election measures. The Bolsa
     Familia rise (R$22bn a year) and the tax lost from the betting ban (R$5.3bn) are
     permanent, Desenrola 3.0 (R$15bn) is a one off in 2027, and free weekend transport (R$16bn
     a year, an estimate from a PT deputy) starts in 2028. Each is divided by nominal GDP.
   Credible fix: the government aims for a primary surplus rising to 2% of GDP by 2029, with
     the average interest rate falling by up to 1.5 points as the central bank cuts. Each path
     draws how much of the plan is actually delivered, a share between 0 and 1 from a
     Beta(4, 2) distribution (two thirds on average), and both the extra surplus and the
     interest rate gain are scaled by that share.

3. Shocks, every year of every path:
   Growth: fat tailed, a Student t with 4 degrees of freedom scaled to the standard deviation of
     Brazil's real growth from 2011 to 2025 excluding 2020 (2.45 points, IMF), so that deep
     recessions like 2015 and 2016 happen more often than a normal curve would allow.
   Interest rate: a random walk with steps of 0.75 points, correlated at minus 0.5 with the
     growth shock, because bad growth years in Brazil tend to come with higher risk premiums.
   Confidence crisis: an 8% chance each year (about two episodes in 25 years, like 2002 and
     2015) that the average interest rate jumps 2.5 points for the rest of the term and growth
     loses 1.5 points that year.
   Budget: the primary balance misses or beats the plan by a normal shock of 0.5 points.

4. 20,000 paths per scenario. Outputs are percentile bands, the chance that debt is lower in
   2030 than in 2026, the chance that it passes 110% of GDP, and the distribution of 2030 debt.
"""
from common import *

style(); h = hand()
rng = np.random.default_rng(2027)
debt = weo("ggxwdg") / 100; prim = weo("ggxonlb") / 100; overall = weo("ggxcnl") / 100; gdp = weo("gdp") / 100
ngdp = pd.read_csv(DATA / "imf_weo_bra_nominal.csv", index_col=0).nominal_gdp_brl_bn
interest = prim - overall
yrs = list(range(2027, 2031)); T = len(yrs)
i_rate = np.array([interest[y] / debt[y - 1] for y in yrs])
n_rate = np.array([ngdp[y] / ngdp[y - 1] - 1 for y in yrs])
sfa = np.array([debt[y] - (debt[y - 1] * (1 + i_rate[k]) / (1 + n_rate[k]) - prim[y]) for k, y in enumerate(yrs)])
base_pb = prim.loc[yrs].values
cost = np.array([(22 + 5.3 + 15) / ngdp[2027]] + [(22 + 5.3 + h["tarifa_zero_cost"]) / ngdp[y] for y in yrs[1:]])
promise_pb = base_pb - cost
fix_target = np.array([0.005, 0.0125, 0.02, 0.02]); fix_i = np.array([-0.005, -0.01, -0.015, -0.015])

N = 20000
sd_g = gdp.loc[2011:2025].drop(2020).std()
t4 = rng.standard_t(4, (N, T)) / np.sqrt(2)          # t(4) has variance 2, so this has unit variance
z = rng.standard_normal((N, T))
g_sh = sd_g * t4
i_steps = 0.0075 * (-0.5 * t4 + np.sqrt(1 - 0.25) * z)
crisis = rng.random((N, T)) < 0.08
crisis_i = np.cumsum(np.where(crisis, 0.025, 0), axis=1)
g_sh = g_sh - np.where(crisis, 0.015, 0)
i_sh = np.cumsum(i_steps, axis=1) + crisis_i
p_sh = rng.normal(0, 0.005, (N, T))
deliver = rng.beta(4, 2, N)[:, None]


def run(pb, i_adj):
    d = np.full(N, debt[2026]); out = np.zeros((N, T))
    for k in range(T):
        d = d * (1 + i_rate[k] + i_adj[:, k] + i_sh[:, k]) / (1 + n_rate[k] + g_sh[:, k]) - (pb[:, k] + p_sh[:, k]) + sfa[k]
        out[:, k] = d
    return out * 100


prom = run(np.tile(promise_pb, (N, 1)), np.zeros((N, T)))
fix = run(base_pb + deliver * (fix_target - base_pb), deliver * fix_i)
d26 = debt[2026] * 100
qs = (5, 25, 50, 75, 95)
pct = pd.concat({"Promises": pd.DataFrame({q: np.percentile(prom, q, axis=0) for q in qs}, index=yrs),
                 "Credible fix": pd.DataFrame({q: np.percentile(fix, q, axis=0) for q in qs}, index=yrs)})
summ = pd.DataFrame({name: {"median_2030": np.median(s[:, -1]), "p5_2030": np.percentile(s[:, -1], 5), "p95_2030": np.percentile(s[:, -1], 95),
                            "p_lower_than_2026": (s[:, -1] < d26).mean() * 100, "p_above_110": (s[:, -1] > 110).mean() * 100,
                            "p_above_120": (s[:, -1] > 120).mean() * 100}
                     for name, s in (("Promises", prom), ("Credible fix", fix))}).T
extra = pd.Series({"debt_2026": d26, "imf_2030": debt[2030] * 100, "promise_cost_2027_pct_gdp": cost[0] * 100,
                   "promise_cost_2028_pct_gdp": cost[1] * 100, "growth_sd_pts": sd_g * 100,
                   "share_paths_with_crisis": crisis.any(axis=1).mean() * 100, "mean_delivery_share": deliver.mean()})
save_table(pct.round(1), "m08_monte_carlo"); save_table(summ.round(1), "m08_summary"); save_table(extra.round(2).to_frame("value"), "m08_inputs")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1.5, 1]})
ax = axes[0]
hist = (debt.loc[2021:2026] * 100)
x = [2026] + yrs
idx = rng.choice(N, 300, replace=False)
for j in idx:
    ax.plot(x, [d26] + list(prom[j]), color=RED, lw=0.7, alpha=0.12)
for j in idx[:120]:
    ax.plot(x, [d26] + list(fix[j]), color=GREEN, lw=0.7, alpha=0.10)
p = pct.loc["Promises"]
ax.fill_between(x, [d26] + list(p[5]), [d26] + list(p[95]), color=RED, alpha=0.13, label="Promises, 90% of paths")
ax.fill_between(x, [d26] + list(p[25]), [d26] + list(p[75]), color=RED, alpha=0.25, label="Promises, 50% of paths")
ax.plot(x, [d26] + list(p[50]), color=RED, lw=2.2, label="Promises, median")
f = pct.loc["Credible fix"]
ax.fill_between(x, [d26] + list(f[25]), [d26] + list(f[75]), color=GREEN, alpha=0.18, label="Credible fix, 50% of paths")
ax.plot(x, [d26] + list(f[50]), color=GREEN, lw=2.2, ls="--", label="Credible fix, median")
ax.plot(hist.index, hist.values, color=INK, lw=2, label="Actual and IMF estimate")
ax.axhline(110, color=INK2, ls=":", lw=1); ax.text(2028.6, 108.4, "110% of GDP", fontsize=7.5, color=INK2)
ax.axvline(2026.5, color=GREY, lw=0.8); ax.text(2026.6, 77, "Fourth term", fontsize=8, color=INK2)
ax.set_xlim(2020.8, 2030.3); ax.set_ylim(75, 135); ax.set_xticks(range(2021, 2031))
ax.set_ylabel("Gross debt, % of GDP (IMF definition)"); ax.legend(fontsize=6.8, loc="upper left", ncol=1, framealpha=0.9)
ax.set_title("Simulated paths, with the bands shaded on top", fontsize=10.5)
ax = axes[1]
bins = np.arange(75, 136, 1.5)
ax.hist(fix[:, -1], bins=bins, color=GREEN, alpha=0.55, density=True, label="Credible fix")
ax.hist(prom[:, -1], bins=bins, color=RED, alpha=0.55, density=True, label="Promises")
ax.axvline(d26, color=INK, lw=1.2); ax.text(d26 - 0.8, ax.get_ylim()[1] * 0.93, "2026", fontsize=8, ha="right")
ax.axvline(110, color=INK2, ls=":", lw=1)
sp, sf = summ.loc["Promises"], summ.loc["Credible fix"]
ax.text(0.98, 0.70, f"Promises\nlower than 2026: {sp.p_lower_than_2026:.0f}%\nabove 110%: {sp.p_above_110:.0f}%", transform=ax.transAxes, ha="right", fontsize=8, color=RED)
ax.text(0.98, 0.45, f"Credible fix\nlower than 2026: {sf.p_lower_than_2026:.0f}%\nabove 110%: {sf.p_above_110:.0f}%", transform=ax.transAxes, ha="right", fontsize=8, color=GREEN)
ax.set_xlabel("Gross debt in 2030, % of GDP"); ax.set_yticks([]); ax.grid(axis="y", visible=False)
ax.legend(fontsize=8, loc="upper left"); ax.set_title("Where debt ends the term", fontsize=10.5)
finish(fig, "Figure 8: On current plans the debt keeps rising through Lula's fourth term",
       "author's model 08, 20,000 paths per scenario; IMF World Economic Outlook (Oct 2026); costs from The Rio Times and Gazeta do Povo.", "fig08_fourth_term.png")
print(summ.round(1)); print(extra.round(2)); print(pct.round(1))
