import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# filter
# conviene defenir como tuple es la manera correcta para pasarle arguementos de python a lenguaje SQL (value,)
release_year = (1985,)

cursor.execute('SELECT * FROM Movies WHERE year=(?)', release_year)
print("mayores a 1985")
print(cursor.fetchall())
connection.commit()
connection.close()