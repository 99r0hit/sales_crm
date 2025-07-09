# backend/auth.py
import sqlite3

def check_login(username, password):
    conn = sqlite3.connect("data/crm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    return bool(result)

def get_user_role(username):
    conn = sqlite3.connect("data/crm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    return result[0] if result else "user"
