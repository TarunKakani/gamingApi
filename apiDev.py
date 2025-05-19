from fastapi import FastAPI, HTTPException, Query
import sqlite3

app = FastAPI()

# errors or additions
# if the search column is bookID and query is any number then it returns every book

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/books')
async def get_books(limit: int = 100, offset: int = 0):
    if limit < 1 or offset < 0:
        raise HTTPException(status_code=400, detail="Invalid limit or offset")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books LIMIT ? OFFSET ?", (limit, offset))
    books = [dict(row) for row in cursor.fetchall()]
    conn.close()
    if not books:
        return {"error": "No books found"}
    return books

@app.get("/books/search")
async def search_books(column: str = Query(...), query: str = Query(...)):
    valid_columns = [
        "bookID", "title", "authors", "average_rating", "isbn",
        "num_pages", "publication_date", "publisher"
    ]
    if column not in valid_columns:
        raise HTTPException(status_code=400, detail="Invalid column name")
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM books WHERE {column} LIKE ?", (f'%{query}%',))
    books = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    if not books:
        return {"error": f"No books found for {column} matching '{query}'"}
    return books

@app.get("/books/{bookID}")
async def get_book(bookID: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE bookID = ?", (bookID,))
    book = cursor.fetchone()
    conn.close()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(book)