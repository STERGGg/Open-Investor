"""
common.py  Shared helpers for the models in Fired for the Machines.
Every model reads only from 03 Data (downloaded market data, or hand_collected_sources.csv
where each row carries its source and URL) and writes to 04 Outputs.
Requirements: python 3.9+, pandas, numpy, matplotlib
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "03 Data"
CHARTS = ROOT / "04 Outputs" / "charts"
TABLES = ROOT / "04 Outputs" / "tables"

for p in (CHARTS, TABLES):
    p.mkdir(parents=True, exist_ok=True)

BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"
GREY, INK, INK2 = "#9a9893", "#0b0b0b", "#52514e"


def style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": "#c9c7c1", "axes.labelcolor": INK2,
        "xtick.color": INK2, "ytick.color": INK2,
        "axes.grid": True, "grid.color": "#e8e6e1", "grid.linewidth": 0.6,
        "axes.titleweight": "bold", "axes.titlesize": 11, "axes.titlelocation": "left",
        "legend.frameon": False, "figure.dpi": 150, "savefig.dpi": 200,
        "lines.linewidth": 2, "axes.axisbelow": True,
    })


def hand():
    df = pd.read_csv(DATA / "hand_collected_sources.csv")
    out = {}
    for k, v in zip(df.key, df.value):
        try:
            out[k] = float(v)
        except (TypeError, ValueError):
            out[k] = v
    return out


def prices():
    """Daily closing prices from Nasdaq via OpenBB: META, MSFT, BCS (Barclays ADR) and QQQ."""
    return pd.read_csv(DATA / "daily_close.csv", index_col=0, parse_dates=True).sort_index()


def fundamentals(kind):
    """Nasdaq fundamentals via OpenBB, kind is 'cash_flow' or 'income'. Values in US$ thousand."""
    df = pd.read_csv(DATA / f"nasdaq_{kind}.csv", parse_dates=["period_ending"])
    return df.sort_values("period_ending")


def bls():
    """Monthly BLS series (CES, CPS and JOLTS), thousands of jobs or % as published."""
    df = pd.read_csv(DATA / "bls_monthly.csv", index_col=0)
    df.index = pd.to_datetime(df.index + "-01")
    return df


def source_note(fig, text):
    fig.text(0.01, 0.005, "Source: " + text, fontsize=7.5, color=INK2, ha="left", va="bottom")


def finish(fig, title, source, fname):
    fig.suptitle(title, x=0.01, ha="left", fontweight="bold")
    source_note(fig, source)
    fig.tight_layout(rect=(0, 0.04, 1, 0.93))
    fig.savefig(CHARTS / fname)
    plt.close(fig)


def save_table(df, name):
    df.to_csv(TABLES / f"{name}.csv")
    return df
