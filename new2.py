import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")

    query = "SELECT * FROM users WHERE username = '" + username + "'"

    result = conn.execute(query)
    return result.fetchone()


def divide(a, b):
    return a / b


password = "admin123"

print(get_user("admin"))
print(divide(10, 0))
