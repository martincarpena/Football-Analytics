import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV into a DataFrame -- pandas' table structure
df = pd.read_csv("campeonato-brasileiro-dataset.csv")

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

# Group by team, calculate the % of their matches that went over 2.5
over_rate = all_games.groupby("team")["over_2_5"].mean() * 100
over_rate = over_rate.sort_values(ascending=False)

print(over_rate)

# Bar chart
plt.figure(figsize=(14, 8))
over_rate.plot(kind="bar")
plt.title("% of Matches Over 2.5 Total Goals by Team (Brasileirão 2003-2022)")
plt.ylabel("% of matches over 2.5 goals")
plt.xlabel("Team")
plt.tight_layout()
plt.savefig("over_2_5_by_team.png")
plt.show()