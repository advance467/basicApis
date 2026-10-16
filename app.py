"""
=============================================================================
Simple Books API (Flask + SQLite)
=============================================================================
A clean, minimal single-file backend for beginners learning APIs.
- Database: SQLite (books.db)
- Operations: CRUD (Create, Read, Update, Delete)
- Format: JSON
=============================================================================
"""

import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------------------------------------------------------------------------
# 1. DATABASE CONNECTION & SETUP
# (check_same_thread=False allows Flask to use this single connection)
# ---------------------------------------------------------------------------
conn = sqlite3.connect("books.db", check_same_thread=False)
conn.row_factory = sqlite3.Row  # Lets us access columns by name (like dictionaries)

# Create table and insert 3 starter books if empty
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
# 2. API ENDPOINTS (CRUD)
# ---------------------------------------------------------------------------



# 1. LIST (Read All)
@app.get("/books")
def get_books():
    rows = conn.execute("SELECT * FROM books").fetchall()
    return jsonify([dict(row) for row in rows])


# 2. SHOW (Read One)
@app.get("/books/<int:book_id>")
def get_book(book_id):
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(dict(row))


# 3. CREATE
@app.post("/books")
def create_book():
    data = request.get_json()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (data["title"], data["author"], int(data["year"])),
    )
    conn.commit()
    return jsonify({"id": cur.lastrowid, **data}), 201


# 4. UPDATE
@app.put("/books/<int:book_id>")
def update_book(book_id):
    data = request.get_json()
    conn.execute(
        "UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?",
        (data["title"], data["author"], int(data["year"]), book_id),
    )
    conn.commit()
    return jsonify({"id": book_id, **data})


# 5. DELETE
@app.delete("/books/<int:book_id>")
def delete_book(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    return jsonify({"message": f"Book {book_id} deleted successfully."})


# ---------------------------------------------------------------------------
# 3. START SERVER
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n=======================================================")
    print("  Backend API Server is starting!")
    print("=======================================================\n")
    app.run(host="0.0.0.0", port=8000, debug=True)
