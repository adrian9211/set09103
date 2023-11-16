import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('# The First Note', 1))
cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('_Another note_', 1))
cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('Visit [this page](https://www.digitalocean.com/community/tutorials) for more tutorials.', 1))

connection.commit()
connection.close()
