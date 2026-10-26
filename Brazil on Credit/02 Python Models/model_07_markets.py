"""
MODEL 07  What the markets were betting on
1. The iShares MSCI Brazil fund (EWZ), Nasdaq daily closes via OpenBB, since January 2025,
   with the first round (4 October) and the last close before the runoff (23 October).
2. The real against the dollar, monthly averages from the Banco Central do Brasil (3698), since
   2018, with the Friday 23 October close (R$4.9654) from The Rio Times.
3. The overnight reaction on 25 and 26 October is reported, not measured: dollar futures up
   about 10% against the real on the CME and a Tokyo listed Ibovespa fund down about 11%
   at the open (The Rio Times), both in thin trading before Brazilian markets reopened.
"""
from common import *

style(); h = hand()
ewz = pd.read_csv(DATA / "ewz_daily_close.csv", index_col=0, parse_dates=True)["close"]
b = bcb()
e = ewz.loc["2025-01-01":]
res = pd.Series({"ewz_2025_start": e.iloc[0], "ewz_oct2": ewz.loc[:"2026-10-02"].iloc[-1], "ewz_oct5": ewz.loc["2026-10-05"],
                 "ewz_oct23": ewz.iloc[-1], "ewz_since_2025_pct": (ewz.iloc[-1] / e.iloc[0] - 1) * 100,
                 "ewz_first_round_day_pct": (ewz.loc["2026-10-05"] / ewz.loc[:"2026-10-02"].iloc[-1] - 1) * 100,
                 "brl_peak_2024_25": b.brl_per_usd.loc["2024":].max(), "brl_oct23": h["brl_close_oct23"]})
save_table(res.round(3).to_frame("value"), "m07_markets")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
ax = axes[0]
ax.plot(e.index, e.values, color=GREEN, lw=1.6)
for d, lab, dy in (("2026-10-05", "First round\n(Flávio ahead)", -4), ("2026-10-23", "Last close\nbefore runoff", 3)):
    y = ewz.loc[:d].iloc[-1]
    ax.annotate(lab, (pd.Timestamp(d), y), (pd.Timestamp(d) - pd.Timedelta(days=120), y + dy), fontsize=7.5, color=INK2,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")); ax.tick_params(axis="x", labelsize=8)
ax.set_ylabel("USD"); ax.set_title("Brazilian shares (EWZ) rallied into the vote", fontsize=10.5)
ax = axes[1]
s = b.brl_per_usd.loc["2018-01-01":].dropna()
ax.plot(s.index, s.values, color=BLUE)
ax.scatter([pd.Timestamp("2026-10-23")], [h["brl_close_oct23"]], color=BLUE, zorder=3)
ax.text(pd.Timestamp("2025-03-01"), h["brl_close_oct23"] - 0.35, f"R${h['brl_close_oct23']:.2f}\non 23 Oct", fontsize=8, color=BLUE)
ax.set_ylabel("Reais per US dollar (higher = weaker real)"); ax.set_title("The real had recovered before the vote", fontsize=10.5)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y")); ax.tick_params(axis="x", labelsize=8)
finish(fig, "Figure 7: Markets had priced in a Bolsonaro win",
       "author's model 07; Nasdaq via OpenBB (EWZ); Banco Central do Brasil SGS 3698; The Rio Times (23 Oct close).", "fig07_markets.png")
print(res.round(3))
