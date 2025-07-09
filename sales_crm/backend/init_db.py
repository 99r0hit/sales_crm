import sqlite3


conn = sqlite3.connect("data/crm.db")
c = conn.cursor()

conn = sqlite3.connect("data/crm.db")
c = conn.cursor()
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", "admin123", "admin"))
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", ("boss", "boss123", "boss"))
c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", ("sales1", "sales123", "user"))
conn.commit()
conn.close()

# Users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)''')

# Opportunities table
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

# Visit plans table
c.execute('''CREATE TABLE IF NOT EXISTS visits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    visit_date TEXT,
    purpose TEXT,
    location TEXT
)''')

conn.commit()
conn.close()
