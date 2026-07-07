import pandas as pd
from pathlib import Path


def load_scorecard():
    """
    Load the final mutual fund scorecard.
    """

    project_root = Path(__file__).resolve().parent.parent

    scorecard = pd.read_csv(
        project_root / "notebooks" / "final_mutual_fund_scorecard_updated.csv"
    )

    return scorecard


def recommend_funds(risk_appetite, top_n=5):
    """
    Recommend top mutual funds based on risk appetite.

    Parameters:
        risk_appetite : Low / Moderate / High
        top_n : Number of funds to recommend

    Returns:
        DataFrame
    """

    scorecard = load_scorecard()

    risk_map = {
        "low": ["Low"],
        "moderate": ["Moderate", "Moderately High"],
        "high": ["High", "Very High"]
    }

    risk = risk_appetite.lower()

    if risk not in risk_map:
        raise ValueError("Risk must be Low, Moderate or High")

    recommendations = (
        scorecard[
            scorecard["risk_category"].isin(risk_map[risk])
        ]
        .sort_values("overall_score", ascending=False)
        .head(top_n)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_category",
            "overall_score"
        ]
    ]


if __name__ == "__main__":

    risk = input("Enter Risk Appetite (Low / Moderate / High): ")

    print("\nRecommended Funds:\n")

    print(recommend_funds(risk))