import sqlite3
from flask import Flask, request

app = Flask(__name__)
db = sqlite3.connect(':memory:', check_same_thread=False)
cursor = db.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
db.commit()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Vulnerable SQL Query (SQL Injection)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)
