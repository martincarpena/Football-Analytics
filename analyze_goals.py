import pandas as pd
import matplotlib.pyplot as plt

# Only teams currently competing in Série A (2026 season)
# Spelled exactly as this dataset writes them -- no accents, Bragantino
# short form, Botafogo-RJ suffix. Mirassol and Remo aren't in this
# dataset yet (data only runs through 2024, both are recent arrivals).
current_serie_a_teams = [
    "Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Bahia",
    "Cruzeiro", "Coritiba", "Atletico-MG", "Bragantino",
    "Corinthians", "Sao Paulo", "Botafogo-RJ", "Vitoria", "Santos",
    "Gremio", "Mirassol", "Vasco", "Internacional", "Remo", "Chapecoense"
]

# Load the CSV into a DataFrame -- pandas' table structure
df = pd.read_csv("campeonato-brasileiro-full.csv")

# Drop any matches missing a score (unplayed/incomplete rows)
df = df.dropna(subset=["mandante_Placar", "visitante_Placar"])

# Total goals in each match = home score + away score
df["total_goals"] = df["mandante_Placar"] + df["visitante_Placar"]

# True/False flag: did this match go over 2.5 total goals?
df["over_2_5"] = df["total_goals"] > 2.5

# Each match involves two teams -- we need one row per team, per match,
# so every team's home AND away games both count.
home_games = df[["mandante", "over_2_5"]].rename(columns={"mandante": "team"})
away_games = df[["visitante", "over_2_5"]].rename(columns={"visitante": "team"})
all_games = pd.concat([home_games, away_games])

# Keep only teams currently in Série A
all_games = all_games[all_games["team"].isin(current_serie_a_teams)]

# Calculate percentage AND match count in one groupby, using .agg()
# "mean" of a True/False column gives the % that were True
# "count" gives how many rows (matches) went into that calculation
team_stats = all_games.groupby("team")["over_2_5"].agg(["mean", "count"])
team_stats["over_2_5_pct"] = team_stats["mean"] * 100
team_stats = team_stats.sort_values("over_2_5_pct", ascending=False)

# Print with both numbers side by side -- this is the whole point:
# a 53% over rate means something different at 400 matches vs 40
print(team_stats[["over_2_5_pct", "count"]].rename(
    columns={"over_2_5_pct": "over_2.5_%", "count": "matches"}
))

# Bar chart -- unchanged, still just the percentage
plt.figure(figsize=(14, 8))
team_stats["over_2_5_pct"].plot(kind="bar")
plt.title("% of Matches Over 2.5 Total Goals by Team (Brasileirão, current Série A teams)")
plt.ylabel("% of matches over 2.5 goals")
plt.xlabel("Team")
plt.tight_layout()
plt.savefig("over_2_5_by_team.png")
plt.show()