import sqlalchemy as db
engine = db.create_engine('sqlite:///movies.db')


connection = engine.connect()

# para cargar una tabla
metadata = db.MetaData()
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)


query = db.select([movies])
# to execute proxi is  the cursor object from the Python database API
# basicamente lo usamos como el cursor para recuperar data
result_proxi = connection.execute(query)

# result set
# podemos interactuar como si fuera un objeto
result_set = result_proxi.fetchall()


print(result_set[0])
print(result_set[:2])


query = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")

result_proxi = connection.execute(query)

result_set = result_proxi.fetchall()

print(result_set[0])


query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year="1960")

connection.execute(query)

query = db.select([movies])
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set)