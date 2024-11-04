import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL, 
        balance INTEGER NOT NULL
        )""")

    connection.commit()
    connection.close()


def add_product(title, description, price):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Products VALUES(NULL, ?, ?, ?)", (title, description, price))
    connection.commit()


def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()

    return products


def add_user(username, email, age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users VALUES(NULL, ?, ?, ?, ?)", (username, email, age, 1000))
    connection.commit()


def get_all_users():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users")
    all_users = cursor.fetchall()

    connection.commit()
    connection.close()
    return all_users


def is_included(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()

    connection.commit()
    connection.close()

    if user is None:
        return False
    else:
        return True


def main():
    initiate_db()
    # for i in range(1, 6):
    #     add_product(f'Продукт {i}', f'Описание {i}', i*100)

    print(get_all_products())
    print(get_all_users())


if __name__ == '__main__':
    main()
