# backend/init_db.py
import sqlite3

conn = sqlite3.connect("data/crm.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)''')

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

c.execute('''CREATE TABLE IF NOT EXISTS visits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    visit_date TEXT,
    purpose TEXT,
    location TEXT
)''')

conn.commit()
