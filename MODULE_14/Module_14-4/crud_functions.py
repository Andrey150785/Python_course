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

def main():
    initiate_db()
    for i in range(1, 6):
        add_product(f'Продукт {i}', f'Описание {i}', i*100)

    print(get_all_products())

if __name__ == '__main__':
    main()
