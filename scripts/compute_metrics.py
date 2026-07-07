import pandas as pd
import numpy as np


def calculate_daily_returns(nav_df):
    """
    Calculate daily returns from NAV history.
    """
    nav_df = nav_df.copy()
    nav_df["date"] = pd.to_datetime(nav_df["date"])
    nav_df = nav_df.sort_values(["amfi_code", "date"])

    nav_df["daily_return"] = (
        nav_df.groupby("amfi_code")["nav"].pct_change()
    )

    return nav_df


def calculate_cagr(nav_df):
    """
    Calculate CAGR for each fund.
    """
    results = []

    for code, group in nav_df.groupby("amfi_code"):
        group = group.sort_values("date")

        start_nav = group["nav"].iloc[0]
        end_nav = group["nav"].iloc[-1]

        years = (group["date"].iloc[-1] - group["date"].iloc[0]).days / 365.25

        cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

        results.append({
            "amfi_code": code,
            "CAGR (%)": round(cagr, 2)
        })

    return pd.DataFrame(results)


def calculate_volatility(nav_df):
    """
    Annualized volatility.
    """
    vol = (
        nav_df.groupby("amfi_code")["daily_return"]
        .std()
        * np.sqrt(252)
        * 100
    )

    return vol.reset_index(name="Volatility (%)")


def calculate_sharpe(nav_df, risk_free_rate=0.06):
    """
    Annualized Sharpe Ratio.
    """
    summary = (
        nav_df.groupby("amfi_code")["daily_return"]
        .agg(["mean", "std"])
        .reset_index()
    )

    summary["Sharpe Ratio"] = (
        (summary["mean"] * 252 - risk_free_rate)
        /
        (summary["std"] * np.sqrt(252))
    )

    return summary[["amfi_code", "Sharpe Ratio"]]


def calculate_max_drawdown(nav_df):
    """
    Maximum Drawdown.
    """
    results = []

    for code, group in nav_df.groupby("amfi_code"):

        nav = group.sort_values("date")["nav"]

        running_max = nav.cummax()

        drawdown = (nav - running_max) / running_max

        results.append({
            "amfi_code": code,
            "Max Drawdown (%)": round(drawdown.min() * 100, 2)
        })

    return pd.DataFrame(results)