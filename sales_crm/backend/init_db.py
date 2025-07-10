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

    # --- Create companies table ---
    c.execute("""CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        turnover TEXT,
        industry TEXT,
        generic_info TEXT,
        hq_location TEXT,
        purchase_office TEXT,
        r_and_d_location TEXT,
        design_location TEXT,
        manufacturing_location TEXT,
        website TEXT,
        country TEXT
    )""")


    
    
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
