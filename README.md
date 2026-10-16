# Books API (Flask)

## Prerequisites

1. **Python (version 3.10 or newer)**: Download from [python.org/downloads](https://www.python.org/downloads/).  
   > ⚠️ **CRITICAL ON WINDOWS:** On the first screen of the installer, you **must check the box**:  
   > `[X] Add python.exe to PATH`

2. **VS Code**: Download from [code.visualstudio.com](https://code.visualstudio.com/).

---

## Step 1: Install Flask

In the terminal, run:

```bash
pip install flask
```

---

## Step 2: Run the API Server

In the terminal, run:

```bash
python app.py
```

*(On Mac/Linux: `python3 app.py`)*

### What happens automatically:
- It creates a local SQLite database file named `books.db` right next to `app.py`.
- It populates it with 3 sample books (*The Hobbit*, *Harry Potter*, *Percy Jackson*).
- It starts the server at `http://127.0.0.1:8000`.

You will see:
```text
>> Database initialized with 3 sample books!

=======================================================
  Backend API Server is starting!
  Open in your browser: http://127.0.0.1:8000/books
  Press CTRL + C to stop.
=======================================================
```
