import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First post', 'Content for first posts'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second post', 'Content for second posts'))

connection.commit()
connection.close()