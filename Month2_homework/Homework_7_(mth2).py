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
        ("Python Basics", "Guido van Rossum", 1991, "Programming", 300, 5),
        ("Clean Code", "Robert C. Martin", 2008, "Programming", 464, 3),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("1984", "George Orwell", 1949, "Dystopia", 328, 6),
        ("War and Peace", "Leo Tolstoy", 1869, "Classic", 1225, 2),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 350, 10),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fable", 96, 4),
        ("The Alchemist", "Paulo Coelho", 1988, "Novel", 208, 5),
        ("Sherlock Holmes", "Arthur Conan Doyle", 1892, "Detective", 450, 3),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 2)
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
