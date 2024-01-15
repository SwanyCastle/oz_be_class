import pymysql

# db connection
connection = pymysql.connect(
    # host = '127.0.0.1',
    host = 'localhost',
    user = 'root',
    password = 'root',
    db = 'classicmodels',
    charset='utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)
# CRUD
# 1. Select
def search_customer(): 
    cursor = connection.cursor()
    
    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()

# 2. Insert
def add_customer():
    cursor = connection.cursor()
    
    name = "seunghwan"
    family_name = "kwak"
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES({1000}, '{name}', '{family_name}')"
    cursor.execute(sql) 
    connection.commit()
    cursor.close()

# add_customer()

# 3. Update
def update_customer():
    cursor = connection.cursor()

    update_name = "update_seunghwan"
    contactLastname = "update_kwak"

    sql = f"UPDATE customers SET customerName='{update_name}',contactLastName='{contactLastname}' WHERE customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# update_customer()
    
# 4. Delete
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# delete_customer()
