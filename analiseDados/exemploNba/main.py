import kagglehub
import pandas as pd

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('C:/Users/Bruno/.cache/kagglehub/datasets/mayabennett03/nba-historical-player-data-1996-2023/versions/1/nba_players.csv')

print("Path to dataset files:", df)

#max college < max other columns 
df['college'].fillna('Unidentifid', inplace=True)

df['team_abbreviation_cod'] = df['team_abbreviation'].astype('category').cat.codes
df['team_cod'] = df['team_abbreviation'].astype(str) + '-' + df['team_abbreviation_cod'].astype(str)
df.info()
