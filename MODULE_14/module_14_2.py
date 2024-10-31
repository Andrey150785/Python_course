import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
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

# ЗАДАНИЕ 14.2

cursor.execute("DELETE FROM Users WHERE id == ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
count_ = cursor.fetchone()[0]
print(count_)

cursor.execute("SELECT SUM(balance) FROM Users")
balance_ = cursor.fetchone()[0]
print(balance_)

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance_ = cursor.fetchone()[0]
print(int(avg_balance_))

connection.commit()
connection.close()