"""
=============================================================================
Simple Books API - Lite Version (Starter)
=============================================================================
A minimal starter file with just:
- Database connection & setup (SQLite)
- A single GET /books endpoint
- Server startup
=============================================================================
"""

import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# ---------------------------------------------------------------------------
# 1. DATABASE CONNECTION & SETUP
# ---------------------------------------------------------------------------
conn = sqlite3.connect("books.db", check_same_thread=False)
conn.row_factory = sqlite3.Row

# Create table and insert starter books if empty
conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
""")

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM books")
if cursor.fetchone()[0] == 0:
    conn.executemany(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        [
            ("The Hobbit", "J.R.R. Tolkien", 1937),
            ("Harry Potter", "J.K. Rowling", 1997),
            ("Percy Jackson", "Rick Riordan", 2005),
        ],
    )
    conn.commit()


# ---------------------------------------------------------------------------
# 2. LIST ALL BOOKS (Read)
# ---------------------------------------------------------------------------
@app.get("/books")
def get_books():
    rows = conn.execute("SELECT * FROM books").fetchall()
    return jsonify([dict(row) for row in rows])


# ---------------------------------------------------------------------------
# 3. START SERVER
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=======================================================")
    print("  Backend API Server is starting!")
    print("=======================================================\n")
    app.run(host="0.0.0.0", port=8000, debug=True)
