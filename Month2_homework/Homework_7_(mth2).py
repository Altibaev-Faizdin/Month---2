import sqlite3

def create_tables():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies
    )
    """)
    connection.commit()
    connection.close()

def insert_books():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    books = [
        ("Манас", "Манасчы", 1800, "Эпос", 5000, 3),
        ("Семетей", "Манасчы", 1850, "Эпос", 4200, 2),
        ("Сейтек", "Манасчы", 1900, "Эпос", 3800, 2),

        ("Жамийла", "Чыңгыз Айтматов", 1958, "Повесть", 128, 7),
        ("Саманчынын жолу", "Чыңгыз Айтматов", 1963, "Повесть", 160, 6),
        ("Ак кеме", "Чыңгыз Айтматов", 1970, "Повесть", 144, 5),
        ("Кылым карытар бир күн", "Чыңгыз Айтматов", 1980, "Роман", 352, 4),
        ("Кассандра тамгасы", "Чыңгыз Айтматов", 1994, "Роман", 384, 3),

        ("Материнское поле", "Чыңгыз Айтматов", 1963, "Роман", 256, 4),
        ("Бетме-бет", "Чыңгыз Айтматов", 1957, "Повесть", 112, 6),
    ]

    cursor.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    create_tables()
    insert_books()
