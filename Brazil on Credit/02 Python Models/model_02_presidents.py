"""
MODEL 02  Presidents compared
Four governments since 2011, using official monthly data from the Banco Central do Brasil
(SGS) and annual growth from the IMF World Economic Outlook (October 2026, with 2026 an IMF
estimate):
  Dilma Rousseff   Jan 2011 to Aug 2016 (impeached)
  Michel Temer     Sep 2016 to Dec 2018
  Jair Bolsonaro   Jan 2019 to Dec 2022
  Lula (third)     Jan 2023 to the latest month
For each: average unemployment (PNAD, from March 2012), average 12 month inflation, average
Selic rate, average real GDP growth (calendar years mostly in the term; 2016 goes to Temer),
the change in gross general government debt (% of GDP) from the month before the term to its
last month, and the change in the real against the dollar over the term.
"""
from common import *

style()
b = bcb(); gdp = weo("gdp")
terms = {"Dilma\n2011 to 2016": ("2011-01-01", "2016-08-01", range(2011, 2016)),
         "Temer\n2016 to 2018": ("2016-09-01", "2018-12-01", range(2016, 2019)),
         "Bolsonaro\n2019 to 2022": ("2019-01-01", "2022-12-01", range(2019, 2023)),
         "Lula\n2023 to 2026": ("2023-01-01", "2026-09-01", range(2023, 2027))}
rows = {}
for name, (s, e, yrs) in terms.items():
    w = b.loc[s:e]
    start_debt = b.gross_gov_debt_pct_gdp.loc[:s].dropna()
    start_debt = start_debt.iloc[-2] if len(start_debt) > 1 else start_debt.iloc[-1]
    end_debt = b.gross_gov_debt_pct_gdp.loc[:e].dropna().iloc[-1]
    rows[name] = {"unemployment_avg": w.unemployment_pct.mean(), "inflation_avg": w.ipca_12m_pct.mean(),
                  "selic_avg": w.selic_pct.mean(), "gdp_growth_avg": gdp.loc[list(yrs)].mean(),
                  "debt_change_pts": end_debt - start_debt, "brl_change_pct": (w.brl_per_usd.dropna().iloc[-1] / b.brl_per_usd.loc[:s].dropna().iloc[-1] - 1) * 100}
t = pd.DataFrame(rows).T
save_table(t.round(2), "m02_presidents")

fig, axes = plt.subplots(1, 4, figsize=(11, 3.9))
spec = [("gdp_growth_avg", "Average growth, %", BLUE), ("unemployment_avg", "Average unemployment, %", ORANGE),
        ("inflation_avg", "Average inflation, %", RED), ("debt_change_pts", "Change in gross debt,\npoints of GDP", VIOLET)]
for ax, (col, title, c) in zip(axes, spec):
    v = t[col]
    ax.bar(range(4), v, color=[GREEN if "Lula" in n else (YELLOW if "Bolsonaro" in n else GREY) for n in t.index], width=0.6)
    for i, val in enumerate(v):
        ax.text(i, val + (0.15 if val >= 0 else -0.6) * (abs(v).max() / 6), f"{val:.1f}", ha="center", fontsize=8)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xticks(range(4)); ax.set_xticklabels([n.split("\n")[0] for n in t.index], fontsize=7.5, rotation=0)
    ax.set_title(title, fontsize=9.5); ax.grid(axis="x", visible=False)
finish(fig, "Figure 2: Four governments compared",
       "author's model 02; Banco Central do Brasil SGS (unemployment, IPCA, debt); IMF WEO Oct 2026 (growth, 2026 estimated).", "fig02_presidents.png")
print(t.round(2))
