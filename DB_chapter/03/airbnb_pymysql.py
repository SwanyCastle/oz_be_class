import pymysql

def execute_pymysql(connection, sql_query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(sql_query, args or ())
        if sql_query.strip().upper().startswith('SELECT'):
            return cursor.fetchall()
        else:
            connection.commit()

def main():
    connection = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'root',
        db = 'airbnb',
        charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor
    )
    
    try:
        # 문제1: 새로운 제품 추가
        # execute_pymysql(connection, "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)", ('Python Book', 29.99, 20))
        # print("새로운 제품 추가")

        # 문제2: 고객 목록 조회
        # result = execute_pymysql(connection, "SELECT * FROM Customers")
        # print("조회 결과")
        # for row in result:
        #     print(row)

        # 문제3: 제품 재고 업데이트
        # execute_pymysql(connection, "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID =%s", (1, 1))
        # print("제품 재고 업데이트")

        # 문제4: 고객별 총 주문 금액 계산
        # result = execute_pymysql(connection, "SELECT c.customerName, SUM(o.totalAmount) AS total_order_price\
        #                              FROM Orders o\
        #                              LEFT JOIN Customers c ON c.customerID = o.customerID\
        #                              GROUP BY c.customerName")
        # for row in result:
        #     print(row)

        # 문제5: 고객 이메일 업데이트
        # execute_pymysql(connection, "UPDATE Customers SET email = %s WHERE customerID = 1", ('first@gmail.com'))
        # print("고객 이메일 업데이트")

        # 문제6: 주문 취소
        # execute_pymysql(connection, "DELETE FROM Orders WHERE orderID = %s", (15))
        # print("주문 취소")

        # 문제7: 특정 제품 검색
        # result = execute_pymysql(connection, "SELECT * FROM Products WHERE productName LIKE %s", ('%Book%'))
        # for row in result:
        #     print(row)

        # 문제8: 특정 고객의 모든 주문 조회
        # result = execute_pymysql(connection, "SELECT * FROM Orders WHERE customerID = %s", (3))
        # for row in result:
        #     print(row)

        # 문제9: 가장 많이 주문한 고객 찾기
        result = execute_pymysql(connection, """SELECT c.customerName, COUNT(o.customerID) AS order_count
                                             FROM Customers c
                                             JOIN Orders o ON o.customerID = c.customerID
                                             GROUP BY c.customerName ORDER BY order_count DESC
                                             LIMIT 1""")
        for row in result:
            print(row)
    finally:
        connection.close()

if __name__ == '__main__':
    main()