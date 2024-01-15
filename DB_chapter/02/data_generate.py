import mysql.connector
from faker import Faker
import random

# MySQL Connection Setting
db_con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='testdatabase'
)

# MySQL Cursor Connection
cursor = db_con.cursor()
faker = Faker()

# users data
for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = 'INSERT INTO users(username, email) VALUES (%s, %s)'
    values = (username, email)
    cursor.execute(sql, values)

# user_id select
cursor.execute("SELECT user_id FROM users")
valid_user_ids = [row[0] for row in cursor.fetchall()]

# ordes data
for _ in range(100):
    user_id = random.choice(valid_user_ids)
    product_name = faker.word()
    quantity = random.randint(1, 10)
    try:
        sql = "INSERT INTO orders (user_id, product_name, quantity) VALUES (%s, %s, %s)"
        values = (user_id, product_name, quantity)
        cursor.execute(sql, values)
    except:
        pass

db_con.commit()
cursor.close()
db_con.close()
