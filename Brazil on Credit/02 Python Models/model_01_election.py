"""
MODEL 01  The election in numbers
1. First round (4 October 2026): share of valid votes for the six main candidates (TSE).
2. Runoffs: 2022 (Lula against Jair Bolsonaro) and 2026 (Lula against Flavio Bolsonaro),
   with the 2026 runoff poll average for comparison.
3. Margin in votes and points.
"""
from common import *

style(); h = hand()
r1 = pd.Series({"Flávio Bolsonaro": h["r1_2026_flavio_pct"], "Lula": h["r1_2026_lula_pct"], "Augusto Cury": h["r1_2026_cury_pct"],
                "Renan Santos": h["r1_2026_santos_pct"], "Ronaldo Caiado": h["r1_2026_caiado_pct"], "Romeu Zema": h["r1_2026_zema_pct"]})
r2 = pd.DataFrame({"Lula": [h["r2_2022_lula_pct"], 100 - h["r2_2026_poll_flavio"], h["r2_2026_lula_pct"]],
                   "Bolsonaro": [h["r2_2022_bolsonaro_pct"], h["r2_2026_poll_flavio"], h["r2_2026_flavio_pct"]]},
                  index=["2022 runoff\n(vs Jair)", "2026 polls\n(vs Flávio)", "2026 runoff\n(vs Flávio)"])
res = pd.Series({"margin_pts": h["r2_2026_lula_pct"] - h["r2_2026_flavio_pct"], "margin_votes": h["r2_2026_lula_votes"] - h["r2_2026_flavio_votes"],
                 "margin_2022_pts": h["r2_2022_lula_pct"] - h["r2_2022_bolsonaro_pct"], "poll_miss_pts": h["r2_2026_lula_pct"] - (100 - h["r2_2026_poll_flavio"])})
save_table(r1.to_frame("first_round_pct"), "m01_first_round"); save_table(r2, "m01_runoffs"); save_table(res.to_frame("value"), "m01_margins")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw={"width_ratios": [1, 1.1]})
ax = axes[0]
cols = [GREEN if k.startswith("Fl") else (RED if k == "Lula" else GREY) for k in r1.index]
ax.barh(r1.index[::-1], r1.values[::-1], color=cols[::-1])
for i, v in enumerate(r1.values[::-1]):
    ax.text(v + 0.6, i, f"{v:.2f}%", va="center", fontsize=8.5)
ax.axvline(50, color=INK2, ls="--", lw=1); ax.text(50.5, 0.1, "50% needed\nto win outright", fontsize=7.5, color=INK2)
ax.set_xlim(0, 60); ax.set_xlabel("% of valid votes"); ax.grid(axis="y", visible=False)
ax.set_title("First round, 4 October", fontsize=11)
ax = axes[1]
x = np.arange(3)
ax.bar(x - 0.18, r2.Lula, 0.36, color=RED, label="Lula")
ax.bar(x + 0.18, r2.Bolsonaro, 0.36, color=GREEN, label="Bolsonaro (Jair in 2022, Flávio in 2026)")
for i, (a, b) in enumerate(zip(r2.Lula, r2.Bolsonaro)):
    ax.text(i - 0.18, a + 0.15, f"{a:.1f}", ha="center", fontsize=8.5); ax.text(i + 0.18, b + 0.15, f"{b:.1f}", ha="center", fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(r2.index, fontsize=8.5); ax.set_ylim(46, 53.5); ax.set_ylabel("% of valid votes")
ax.legend(fontsize=7.5, loc="upper left"); ax.grid(axis="x", visible=False)
ax.set_title("The polls had Flávio ahead. Lula won", fontsize=11)
finish(fig, "Figure 1: Brazil's 2026 presidential election",
       "author's model 01; TSE results via TSE and The Rio Times; 2026 runoff poll average (45 polls) via The Rio Times; 2022 result via Wikipedia.", "fig01_election.png")
print(r1); print(r2); print(res)
