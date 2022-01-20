import psycopg2

def insert_sale(conn, order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount):
	order_total = quantity * price
	if discount	!= 0:
		order_total	 = order_total * discount
	sale_data = (order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount, order_total)
	cur = conn.cursor()
	cur.execute(''' DELETE FROM SALES WHERE ORDER_NUM=1''')
	cur = conn.cursor()
	cur.execute(""" INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
	(%s, %s, %s, %s, %s, %s, %s, %s, %s)

	""",sale_data)

	# cur = conn.cursor()
	# cur.execute(""" INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
	# (?, ?, ?, ?, ?, ?, ?, ?, ?)

	# """,sale_data)

	conn.commit()

	cur.execute("""SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=%s""",(order_num,))

	rows = cur.fetchall()
	for row in rows:
		print("CUST_NAME = ", row[0])
		print("ORDER_TOTAL =", row[1], "\n")


if __name__ == '__main__':
	conn = psycopg2.connect(database="red30",
		user="postgres",
		password="password",
		host="localhost",
		port="5432")
	

	order_num = int(input("What is the order number?"))
	order_type = input("What is the order type: Retail or Wholesale?\n")
	cust_name = input("What adasdd")
	prod_number = input("adsada")
	prod_name = input("what is")
	quantity = float(input("adada"))
	price = float(input("dasdasda"))
	discount = float(input("asdasds"))

	insert_sale(conn, order_num, order_type, cust_name, prod_number, prod_name, quantity, price, discount)
	conn.close()
