import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (content) VALUES (?)", ('# The First Note',))
cur.execute("INSERT INTO notes (content) VALUES (?)", ('# Second Note',))
cur.execute("INSERT INTO notes (content) VALUES (?)", ('# Third Note',))
cur.execute("INSERT INTO notes (content) VALUES (?)", ('# Fourth Note',))
cur.execute("INSERT INTO User (email) VALUES (?)", ('adrian9211@gmail.com',))


connection.commit()
connection.close()
