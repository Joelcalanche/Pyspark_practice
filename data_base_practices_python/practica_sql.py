import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1976)")

# cursor.execute("SELECT * FROM Movies")

famausFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
			   ('Back to future', 'Steven Spielberg', 1985),
			   ('Moonrise Kingdom', 'Wes Anderson', 2012)]
#? es un placeholder
# cursor.executemany('Insert Into Movies VALUES (?,?,?)', famausFilms)
records = cursor.execute("SELECT * FROM Movies")

# print(cursor.fetchone())
# con esto veo todos los registros
print("utilizando fetchall")
# print(cursor.fetchall())# is most faster

# tambien puedo hacer un for loop
print("\nutilizando for loop")
for record in records:
	print(record)

cursor.fetchone()# debera dar enty porque el cursos se ha movido a la ultima posicion

# al guardar el resultado de la busqueda en record tenemos una hemos pasado una referencia del cursor y podemos iterar dos veces 
connection.commit()
connection.close()