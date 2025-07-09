import sqlite3
import bcrypt

def check_login(username, password):
    conn = sqlite3.connect("data/crm.db")
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()

    if row:
        hashed = row[0]
        return bcrypt.checkpw(password.encode(), hashed.encode())
    return False

def get_user_role(username):
    conn = sqlite3.connect("data/crm.db")
    cur = conn.cursor()
    cur.execute("SELECT role FROM users WHERE username=?", (username,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else "user"
