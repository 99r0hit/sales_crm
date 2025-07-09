import sqlite3
import os
import bcrypt

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/crm.db")
    c = conn.cursor()

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')

    # Create opportunities table
    c.execute('''CREATE TABLE IF NOT EXISTS opportunities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        product TEXT,
        industry TEXT,
        interest TEXT,
        description TEXT,
        qty INTEGER,
        price REAL,
        sop_stage INTEGER,
        created_by TEXT
    )''')

    # Create visits table
    c.execute('''CREATE TABLE IF NOT EXISTS visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        visit_date TEXT,
        purpose TEXT,
        location TEXT
    )''')

    # Add default users (optional)
    def add_user(username, password, role):
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        try:
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_pw, role))
        except:
            pass  # If user already exists

    add_user("admin", "admin123", "admin")
    add_user("boss", "boss123", "boss")
    add_user("sales1", "sales123", "user")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
