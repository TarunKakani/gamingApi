import sqlite3
import pandas as pd

# Path to the gaming dataset
DATABASE_PATH = './gamesDataset/steam_games.csv'
DATABASE = 'games.db'

# connect to sqlite
try:
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    print("Database connected.")

except sqlite3.DatabaseError:
    print("Database not connected")

# Load the database using pandas
df = pd.read_csv(DATABASE_PATH)

# Inspect and check the dataset
print(df.head())

# create the table if it doesn't exist

try:
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT,
        platform TEXT,
        release_year INTEGER
    )
''')
    
    print("Table created!")

except sqlite3.SQLITE_CREATE_TABLE:
    print("Table already exists continuing!")


try:
    for _, row in df.iterrows():
        
        tittle = row['name']
        genre = row['genres']
        platform = row['platforms']
        releaseDate = row['release_date']

        cursor.execute(''' 
            INSERT INTO games (title, genre, platform, release_year)
            VALUES (?, ?, ?, ?)
         ''', (tittle, genre, platform, releaseDate))