import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRYMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")
for i in range(1, 11):
    cursor.execute("INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", i*10, 1000))

cursor.execute("UPDATE users SET balance = ? WHERE (age/10) % 2 != 0", ("500",))

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE AGE = ?", (i*10,))

cursor.execute("SELECT username, email, age, balance FROM users WHERE AGE != 60")
users = cursor.fetchall()

for user in users:
    username, email, age, balance = user
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

connection.commit()
connection.close()