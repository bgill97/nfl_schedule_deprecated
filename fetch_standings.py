import nflreadpy as nfl
import pandas as pd

pd.set_option('display.max_columns', None)

games = nfl.load_schedules(2026).to_pandas()
print(games.columns)

#remove unnecessary columns
games = games.drop(columns=["game_id","season",'game_type', 'week', 'gameday', 'weekday', 'gametime', 'location', 'total', 'overtime', 'old_game_id', 'gsis', 'nfl_detail_id', 'pfr', 'pff', 'espn', 'ftn', 'away_rest', 'home_rest', 'away_moneyline', 'home_moneyline', 'spread_line', 'away_spread_odds', 'home_spread_odds', 'total_line', 'under_odds', 'over_odds', 'div_game', 'roof', 'surface', 'temp', 'wind', 'away_qb_id', 'home_qb_id', 'away_qb_name', 'home_qb_name', 'away_coach', 'home_coach', 'referee', 'stadium_id', 'stadium'])

#drop nulls
games = games.dropna(how="any")

#add W/L columns
for index,row in games.iterrows():
    if row['away_score'] > row['home_score']:
        games.at[index,'away_team_win'] = 1
        games.at[index,'home_team_win'] = 0
    elif row['home_score'] > row['away_score']:
        games.at[index,'away_team_win'] = 0
        games.at[index,'home_team_win'] = 1
    elif row['home_score'] == row['away_score']:
        games.at[index,'away_team_win'] = 0
        games.at[index,'home_team_win'] = 0
        games.at[index,'away_team_win'] = 1
        games.at[index,'home_team_win'] = 1
    else:
        raise TypeError('Could not evaluate the scores of the game.')

teams = games['away_team'].unique()

standings = pd.DataFrame(columns=["team","w","l"])
print(games)

for team in teams:
    pass