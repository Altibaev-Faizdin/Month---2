import sqlite3

def create_table(connection):
    connection.execute(""" create a database connection""")

if __name__=="__main__":
    connection = sqlite3.connect('database.db')
