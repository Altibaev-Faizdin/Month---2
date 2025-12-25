import sqlite3

conn = sqlite3.connect('books.db')


def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    conn.commit()


def insert_books():
    books = [
        ('Манас', 'Манасчы', 1800, 'Эпос', 5000, 3),
        ('Семетей', 'Манасчы', 1850, 'Эпос', 4200, 2),
        ('Сейтек', 'Манасчы', 1900, 'Эпос', 3800, 2),

        ('Жамийла', 'Чыңгыз Айтматов', 1958, 'Повесть', 128, 7),
        ('Саманчынын жолу', 'Чыңгыз Айтматов', 1963, 'Повесть', 160, 6),
        ('Ак кеме', 'Чыңгыз Айтматов', 1970, 'Повесть', 144, 5),
        ('Кылым карытар бир күн', 'Чыңгыз Айтматов', 1980, 'Роман', 352, 4),
        ('Кассандра тамгасы', 'Чыңгыз Айтматов', 1994, 'Роман', 384, 3),

        ('Материнское поле', 'Чыңгыз Айтматов', 1963, 'Роман', 256, 4),
        ('Бетме-бет', 'Чыңгыз Айтматов', 1957, 'Повесть', 112, 6),
    ]

    conn.executemany("""
        INSERT INTO books
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)
    conn.commit()


def delete_books(book_id):
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()


def edit_books(book_id, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
        UPDATE books
        SET name = ?, author = ?, publication_year = ?, genre = ?,
            number_of_pages = ?, number_of_copies = ?
        WHERE id = ?
    """, (name, author, publication_year, genre,
          number_of_pages, number_of_copies, book_id))
    conn.commit()


def get_all_books():
    result = conn.execute("SELECT * FROM books")
    return result.fetchall()


if __name__ == '__main__':
    create_table()
    insert_books()

    delete_books(2)
    edit_books(4, 'Жамийла', 'Чыңгыз Айтматов',
               1958, 'Повесть', 130, 6)

    print("ВСЕ КНИГЫ:")
    for book in get_all_books():
        print(book)

    conn.close()

