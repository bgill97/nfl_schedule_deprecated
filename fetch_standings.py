import pandas as pd

pd.set_option('display.max_columns', None)

url = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
games = pd.read_csv(url)
games = games[games["season"] == 2026]

teams = games['away_team'].unique().tolist()

games = games.dropna(subset=["away_score","home_score"])

standings = pd.DataFrame({"team": teams,"w": 0,"l": 0,"t": 0}).set_index("team")


# #remove unnecessary columns
# games = games.drop(columns=["game_id","season",'game_type', 'week', 'gameday', 'weekday', 'gametime', 'location', 'total', 'overtime', 'old_game_id', 'gsis', 'nfl_detail_id', 'pfr', 'pff', 'espn', 'ftn', 'away_rest', 'home_rest', 'away_moneyline', 'home_moneyline', 'spread_line', 'away_spread_odds', 'home_spread_odds', 'total_line', 'under_odds', 'over_odds', 'div_game', 'roof', 'surface', 'temp', 'wind', 'away_qb_id', 'home_qb_id', 'away_qb_name', 'home_qb_name', 'away_coach', 'home_coach', 'referee', 'stadium_id', 'stadium'])


#add W/L columns
for _,row in games.iterrows():
    away,home = row["away_team"],row["home_team"]
    if row['away_score'] > row['home_score']:
        standings.loc[away,"w"] += 1
        standings.loc[home,"l"] += 1
    elif row['home_score'] > row['away_score']:
        standings.loc[away,"l"] += 1
        standings.loc[home,"w"] += 1
    elif row['home_score'] == row['away_score']:
        standings.loc[away,"t"] += 1
        standings.loc[home,"t"] += 1
    else:
        raise TypeError('Could not evaluate the scores of the game.')

standings = standings.sort_values(["w","t"],ascending=False)
print(standings)

