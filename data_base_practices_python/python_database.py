import sqlite3
# si no existe la crea 
connection = sqlite3.connect('movies.db')

cursor = connection.cursor()


cursor.execute("""

				CREATE TABLE IF NOT EXISTS	Movies
				(Title TEXT, Director TEXT, Year INT)		




	""")

connection.commit()

connection.close()



