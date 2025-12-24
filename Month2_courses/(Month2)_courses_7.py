import sqlite3
from pprint import pprint


def create_tables(connection):
    connection.execute("DROP TABLE IF EXISTS students")
    connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER DEFAULT 0,
        city TEXT
    )
    """)


def add_student(connection, name, age, city):
    connection.execute(
        """
        INSERT INTO students (name, age, city)
        VALUES (?, ?, ?)
        """,
        (name, age, city)
    )
    connection.commit()


def delete_student(connection, student_id):
    connection.execute(
        """
        DELETE FROM students WHERE id = ?
        """,
        (student_id,)
    )
    connection.commit()


def get_all_students(connection):
    result = connection.execute(
        "SELECT id, name FROM students"
    )
    return result.fetchall()


def get_student(connection, student_id):
    result = conn.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    return result.fetchone()

def get_students_by_city(connection, city):
    result = conn.execute(
        """
        SELECT * FROM students 
        WHERE city = ?
        ORDER BY age
        """,
        (city,)
    )
    return result.fetchall()


def change_student(connection, student_id, name, age, city):
    connection.execute(
    """
    UPDATE students SET name = ?, age = ?, city = ? WHERE id = ? 
    """,
        (name, age, city, student_id)
    )
    connection.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables(conn)
    add_student(conn, "Alinur", 21, "Bishkek")
    add_student(conn, "Igor", 21, "Sokuluk")
    add_student(conn, "Artur", 25, "Karakol")
    add_student(conn, "Aisuluu", 20, "Bishkek")

    delete_student(conn, 2)

    pprint(get_all_students(conn))
    for st in get_all_students(conn):
        print(st)

    print(get_student(conn, 3))
    pprint(get_students_by_city(conn, "Bishkek"))

    change_student(conn, 3, "Artur", 20, "Bishkek")
    print(get_student(conn, 3))

    conn.close()