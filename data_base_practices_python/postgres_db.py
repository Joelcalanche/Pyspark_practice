import psycopg2

conn = psycopg2.connect(database="red30",
	user="postgres",
	password="password",
	host="localhost",
	port="5432")

cursor = conn.cursor()

 # cursor.execute("""

#  		CREATE TABLE Sales
#  		(ORDER_NUM INT PRIMARY KEY,
#  				ORDER_TYPE TEXT,
#  				CUST_NAME TEXT,
#  				PROD_NUMBER TEXT,
#  				PROD_NAME TEXT,
#  				QUANTITY INT,
#  				PRICE REAL,
#  				DISCOUNT REAL,
#  				ORDER_TOTAL REAL);

#  	""")

# cursor.execute("SELECT * FROM SALES LIMIT 10")

# print(cursor.fetchall())

# cursor.execute(""" INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
# 	(1105910, 'Retail', 'syman Mapstone', 'EB521', 'Understanding Artificial Intelligence', 3, 19.4, 0, 58.5)

# 	""")



# conn.commit()
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=1105910")
rows = cursor.fetchall()
for row in rows:
	print("CUST_NAME=", row[0])
	print("ORDER_TOTAL", row[1], "\n")




conn.close()




# \copy sales FROM  'path/file.csv' WITH DELIMETER ',' CSV HEADER;
