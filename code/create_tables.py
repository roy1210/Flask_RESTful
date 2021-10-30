import sqlite3

connection = sqlite3.connect('data.db')

# image -> cursor in CLI
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

# save
connection.commit()

# good practice about ensure no more data coming
connection.close()
