import pandas as pd


def load_data():
    games = pd.read_csv("data/raw/Games.csv", low_memory=False)
    team_stats = pd.read_csv("data/raw/TeamStatistics.csv", low_memory=False)
    return games, team_stats


def compute_team_win_percentage(games):
    games["season"] = pd.to_datetime(games["gameDate"], errors="coerce", utc=True).dt.year

    games["winner"] = games["winner"].astype(str)

    wins = (
        games.groupby(["season", "winner"])["gameId"]
        .count()
        .reset_index()
        .rename(columns={"winner": "team_name", "gameId": "wins"})
    )

    total_games = pd.concat([
        games[["season", "hometeamName"]].rename(columns={"hometeamName": "team_name"}),
        games[["season", "awayteamName"]].rename(columns={"awayteamName": "team_name"})
    ])
    total_games["team_name"] = total_games["team_name"].astype(str)

    total_games = (
        total_games.groupby(["season", "team_name"])
        .size()
        .reset_index(name="games_played")
    )

    merged = total_games.merge(wins, on=["season", "team_name"], how="left").fillna(0)
    merged["win_pct"] = merged["wins"] / merged["games_played"]

    return merged


def merge_team_data(team_stats, win_pct):
    team_stats["season"] = pd.to_datetime(team_stats["gameDate"], errors="coerce", utc=True).dt.year

    team_stats.rename(columns={"teamName": "team_name"}, inplace=True)

    for df in [team_stats, win_pct]:
        df["season"] = df["season"].astype(str)
        df["team_name"] = df["team_name"].astype(str)

    merged = pd.merge(team_stats, win_pct, on=["season", "team_name"], how="left")
    return merged


def build_full_dataset():
    games, team_stats = load_data()
    win_pct = compute_team_win_percentage(games)
    full_dataset = merge_team_data(team_stats, win_pct)
    full_dataset.to_csv("data/processed/full_dataset.csv", index=False)
    print("Full Dataset Done")
    return full_dataset


if __name__ == "__main__":
    build_full_dataset()
