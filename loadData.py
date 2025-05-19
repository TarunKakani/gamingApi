import sqlite3
import pandas as pd

df = pd.read_csv("books_cleaned.csv")

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        bookID INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        authors TEXT NOT NULL,
        average_rating REAL NOT NULL,
        isbn TEXT NOT NULL,
        num_pages INTEGER NOT NULL,
        publication_date TEXT NOT NULL,
        publisher TEXT NOT NULL
    )
''')

df.to_sql('books', conn, if_exists='replace', index=False)

conn.commit()
conn.close()