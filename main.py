import sqlite3


connection = sqlite3.connnect('zoo.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS animals ('
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NIT NULL,
    age INTEGER
)
''')

cursor.execute(
    'INSERT INTO animals (name, species, age) VALUES ('Лев', 'Хищник', '9'))'

cursor.execute('SELECT * FROM animals')
rows = cursor.fetchall()
for row in rows:
print(row)

connection.commit()
connection.close()
