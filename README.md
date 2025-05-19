# Gaming Database API

This project is a gaming database API built with **FastAPI** and **SQLite3**. The database is populated directly from a CSV dataset file.

## Features

- RESTful API for accessing gaming data
- Search functionality on various columns
- FastAPI for high performance
- SQLite3 as the database backend

## Setup

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlite3
    ```
3. Run the API:
    ```bash
    uvicorn main:app --reload
    ```

## Endpoints

### Search Books

- **Endpoint:** `/books/search`
- **Parameters:**
  - `column`: The column to search (e.g., `bookID`)
  - `query`: The search value

#### Example

```
GET /books/search?column=bookID&query=1
```

**Note:**  
Currently, this returns all books where the query number exists anywhere in the specified column, not just exact matches.

## Known Issues

- The search endpoint may return partial matches instead of exact matches.
- More robust error handling is needed for invalid queries and parameters.

## To Do

- Improve search logic for exact matches.
- Add comprehensive error handling and validation.
- Expand API documentation.
- Host the API on a cloud platform (e.g., Heroku, Render).
- Publish the API to RapidAPI.