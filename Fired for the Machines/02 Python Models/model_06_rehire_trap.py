"""
MODEL 06  The rehire trap, a Monte Carlo
What does a company really save when it cuts jobs because AI will do the work? Every role costs 1
(one year of its pay) and the horizon is three years, so a cut that sticks would save 3 per role.
50,000 imaginary companies each cut a block of roles, and for each one the model draws:

  severance           0.25 to 0.6 of a year's pay (Meta pays 16 weeks plus 2 a year of service)
  AI tools            0.1 to 0.4 of the removed pay every year, for software, compute and staff to run it
  rehire or not       two in three companies bring people back (Careerminds survey of 600 HR leaders)
  share rehired       Beta(2,2) for those that do, so half rehire more than half the roles, in line
                      with the survey's finding that over a third of all cutters rehired over half
  months until rehire lognormal with a median of 6 months, as 52% of rehirers did it within six
  cost of rehiring    0.3 to 0.8 of a year's pay per role (recruiting, onboarding, lost output while
                      new people learn the job)
  pay of rehires      0.85 to 1.15 of the old pay (some roles go offshore, some cost more)
  damage while short  0 to 0.5 of a year's pay per year for each role that turned out to be needed,
                      for the months it was empty (complaints, errors, overtime)

Net saving over three years is reported as a share of the promised saving. A company has lost money
if the net is below zero, is roughly even if it kept less than a third of what it promised, and is
ahead otherwise. These bands are my own definitions and are compared with the Careerminds answers
(30.9% spent more on rehiring than they saved, 42.4% roughly cancelled out, about a quarter ahead).
The survey reports these shares in the context of companies that brought staff back, so the chart
compares them with the simulated companies that rehired. Across all simulated cutters, including those
that never rehire, the picture is better, and both are saved in the table.
The last step applies the median outcome to Meta's 8,000 cuts.
"""
from common import *

style(); h = hand()
rng = np.random.default_rng(42)
N, H = 50_000, 3.0
sev = rng.uniform(0.25, 0.6, N)
ai = rng.uniform(0.1, 0.4, N)
rehire = rng.random(N) < h["cm_rehiring_share"]
share = np.where(rehire, rng.beta(2, 2, N), 0.0)
months = np.clip(rng.lognormal(np.log(6), 0.7, N), 1, 30)
rcost = rng.uniform(0.3, 0.8, N)
paym = rng.uniform(0.85, 1.15, N)
dmg = rng.uniform(0.0, 0.5, N)

t = months / 12
kept = H - sev - ai * H                                     # role stays cut
back = t - sev - ai * H - rcost - (H - t) * (paym - 1) - dmg * t   # role cut then refilled
net = (1 - share) * kept + share * back
pct = net / H * 100
promised_ideal = (H - sev - ai * H) / H * 100

lost = (pct < 0).mean(); even = ((pct >= 0) & (pct < 100 / 3)).mean(); ahead = (pct >= 100 / 3).mean()
pr = pct[rehire]
lost_r = (pr < 0).mean(); even_r = ((pr >= 0) & (pr < 100 / 3)).mean(); ahead_r = (pr >= 100 / 3).mean()
comp = pd.DataFrame({"model_all_cutters": [lost * 100, even * 100, ahead * 100], "model": [lost_r * 100, even_r * 100, ahead_r * 100],
                     "careerminds_survey": [h["cm_spent_more"] * 100, h["cm_roughly_even"] * 100, 100 - (h["cm_spent_more"] + h["cm_roughly_even"]) * 100]},
                    index=["Lost money", "Roughly even", "Came out ahead"])
cost_per_dollar = ((sev + ai * H + share * (rcost + (H - t) * (paym - 1) + dmg * t)) / (H - share * (H - t))).mean()
meta_promised = h["meta_cut_apr26"] * h["meta_median_pay_2025"] / 1e9 * H
res = pd.Series({"median_net_pct_of_promised": np.median(pct), "mean_net_pct": pct.mean(), "p10": np.percentile(pct, 10), "p90": np.percentile(pct, 90),
                 "share_lost_pct_all": lost * 100, "share_lost_pct_rehirers": lost_r * 100, "share_ahead_pct_rehirers": ahead_r * 100, "share_even_pct": even * 100, "share_ahead_pct": ahead * 100,
                 "no_rehire_median_pct": np.median(pct[~rehire]), "rehire_median_pct": np.median(pct[rehire]),
                 "mean_cost_per_dollar_of_saving": cost_per_dollar, "orgvue_cost_per_dollar": h["orgvue_cost_per_dollar"],
                 "meta_3yr_promised_usd_bn": meta_promised, "meta_3yr_median_net_usd_bn": meta_promised * np.median(pct) / 100})
save_table(comp.round(1), "m06_vs_survey"); save_table(res.round(2).to_frame("value"), "m06_summary")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw={"width_ratios": [1.4, 1]})
ax = axes[0]
bins = np.arange(-60, 101, 2.5)
ax.hist(pct[~rehire], bins=bins, color=GREEN, alpha=0.6, label="Companies that never rehire", density=False)
ax.hist(pct[rehire], bins=bins, color=RED, alpha=0.55, label="Companies that bring people back", density=False)
ax.axvline(0, color=INK, lw=1); ax.axvline(100 / 3, color=INK2, ls=":", lw=1)
ax.text(-58, 1650, "lost money", fontsize=8, color=INK2)
ax.text(2, 1700, "roughly\neven", fontsize=8, color=INK2, va="top")
ax.text(36, 1650, "ahead", fontsize=8, color=INK2)
ax.set_xlabel("Net three year saving, % of what the cut promised"); ax.set_ylabel("Number of simulated companies")
ax.set_ylim(0, 2100); ax.legend(fontsize=7.5, loc="upper right"); ax.set_title("Bringing people back wipes out most of the saving", fontsize=10.5)
ax = axes[1]
x = np.arange(3)
ax.bar(x - 0.19, comp.model, 0.38, color=BLUE, label="My model, firms that rehire")
ax.bar(x + 0.19, comp.careerminds_survey, 0.38, color=GREY, label="Survey of HR leaders")
for j in range(3):
    ax.text(j - 0.19, comp.model.iloc[j] + 1, f"{comp.model.iloc[j]:.0f}%", ha="center", fontsize=8)
    ax.text(j + 0.19, comp.careerminds_survey.iloc[j] + 1, f"{comp.careerminds_survey.iloc[j]:.0f}%", ha="center", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(comp.index, fontsize=8.5); ax.set_ylim(0, 60); ax.set_ylabel("% of companies")
ax.legend(fontsize=8, loc="upper right"); ax.grid(axis="x", visible=False)
ax.set_title("The model lands close to what firms report", fontsize=10.5)
finish(fig, "Figure 6: Most AI layoffs save far less than promised",
       "author's model 06, 50,000 simulated companies; Careerminds survey of 600 HR leaders (Feb 2026) via IBTimes; Meta severance terms via SiliconANGLE.", "fig06_rehire_trap.png")
print(comp.round(1)); print(res.round(2))
