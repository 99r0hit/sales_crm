import sqlite3
import bcrypt

def add_user(username, password, role):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conn = sqlite3.connect("data/crm.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, hashed_pw, role))
    conn.commit()
    conn.close()
    print(f"✅ User '{username}' added.")

# Example usage:
add_user("admin", "admin123", "admin")
add_user("boss", "boss123", "boss")
add_user("sales1", "sales123", "user")
