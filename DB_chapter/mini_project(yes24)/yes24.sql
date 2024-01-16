USE yes24;

-- CREATE TABLE Books (
--     bookID INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     author VARCHAR(255),
--     publisher VARCHAR(255),
--     publishing DATE,
--     rating DECIMAL(3, 1),
--     review INT,
--     sales INT,
--     price DECIMAL(10, 2),
--     ranking INT,
--     ranking_weeks INT
-- );

-- 기본 조회 및 필터링
-- SELECT title, author FROM Books
-- SELECT * FROM Books WHERE rating <= 8.0;
-- SELECT title, review FROM Books WHERE review >= 100;
-- SELECT title, price FROM Books WHERE price < 20000;
-- SELECT title, ranking, ranking_weeks FROM Books WHERE ranking_weeks >= 4;
-- SELECT * FROM Books WHERE author LIKE '%최태성%';
-- SELECT * FROM Books WHERE publisher LIKE '%이투스%';

-- 조인 및 관계
-- SELECT author, COUNT(*) AS books FROM Books GROUP BY author;
-- SELECT publisher, COUNT(*) AS published_book FROM Books GROUP BY publisher ORDER BY published_book DESC LIMIT 1;
-- SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;
-- SELECT title, author FROM Books WHERE ranking = 1;
-- SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;
-- SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5;

-- 집계 및 그룹화
-- SELECT author, AVG(rating) AS author_rating FROM Books GROUP BY author;
-- SELECT publishing, COUNT(*) AS published_books FROM Books GROUP BY publishing;
-- SELECT title, AVG(price) AS avg_price FROM Books GROUP BY title;
-- SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;
-- SELECT ranking, AVG(review) AS avg_review FROM Books GROUP BY ranking;

-- 서브쿼리 및 고급 기능
-- SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);
-- SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);
-- SELECT title, review FROM Books WHERE review > (SELECT MAX(review) FROM Books);
-- SELECT title, sales FROM Books WHERE sales > (SELECT AVG(sales) FROM Books);
-- SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;

-- 데이터 수정 및 관리
-- UPDATE Books SET price = 1 WHERE bookID = 1;
-- UPDATE Books SET title = "조정래" WHERE author LIKE "%조정래%";
-- DELETE FROM Books WHERE sales = (SELECT sales FROM (SELECT MIN(sales) FROM Books) AS min_sales); -- 데이터 전체 다 지워짐 왜 ?
-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books); -- 이건 오류남
-- SELECT title, sales FROM Books ORDER BY sales ASC;
-- UPDATE Books SET rating = rating + 1 WHERE publisher = "이투스북";

-- 데이터 분석 예제
-- SELECT author FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY AVG(rating) DESC LIMIT 1) ORDER BY sales DESC LIMIT 1;
-- SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author ORDER BY avg_rating DESC, avg_sales DESC LIMIT 1;
-- SELECT publishing, AVG(price) FROM Books GROUP BY publishing ORDER BY publishing ASC;
-- SELECT publisher, COUNT(title) AS publish_books, AVG(review) AS avg_review FROM Books GROUP BY publisher ORDER BY publish_books DESC, avg_review DESC;
-- SELECT publisher, COUNT(title) AS publish_books, SUM(review) AS sum_review FROM Books GROUP BY publisher ORDER BY publish_books DESC, sum_review DESC;
-- SELECT ranking, AVG(sales) FROM Books GROUP BY ranking;
-- SELECT price, AVG(review), AVG(rating) FROM Books GROUP BY price;

-- 난이도 있는 문제
-- SELECT publisher, author, AVG(sales) AS avg_sales FROM Books GROUP BY publisher, author ORDER BY avg_sales DESC;
-- SELECT publisher, author, AVG(sales) as avg_sales
-- FROM Books
-- GROUP BY publisher, author
-- ORDER BY avg_sales DESC;
-- SELECT title, review, price FROM Books WHERE review > (SELECT AVG(review) FROM Books) and price < (SELECT AVG(price) FROM Books);
-- SELECT title, review, price
-- FROM Books
-- WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);
-- SELECT author, COUNT(DISTINCT title) AS count_books FROM Books GROUP BY author ORDER BY count_books DESC LIMIT 1;
-- SELECT author, MAX(sales) AS top_sales FROM Books GROUP BY author ORDER BY author, top_sales DESC;
-- SELECT year(publishing) as year, COUNT(*) AS published_count, AVG(price) AS avg_price FROM Books GROUP BY year ORDER BY year DESC;
-- SELECT publisher, COUNT(*) AS count, MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- HAVING count >= 2
-- ORDER BY rating_difference DESC;
-- SELECT title, sales, rating, rating / sales as ratio
-- FROM Books
-- ORDER BY ratio DESC;





