use sakila;

-- 데이터 조회 및 필터링
-- 1번 문제

-- 내가 푼 방법
-- select f.title from film f 
-- join film_actor fa on fa.film_id = f.film_id 
-- where fa.actor_id = 
-- (select actor_id from actor where last_name = 'GUINESS' and first_name = 'PENELOPE');

-- 정답
-- SELECT f.title
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS';

-- 2번
-- 내가 푼 방법 (결과는 같은데 카테고리 이름 표시 X, 카테고리 아이디만 표시))
-- select fc.category_id, COUNT(*) as count_film_id from film_category fc group by fc.category_id;

-- 정담 (카테고리 이름 표시됨)
-- SELECT c.name, COUNT(fc.film_id) as number_of_films
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- GROUP BY c.name;

-- 3번 문제
-- 내가 푼 방법
-- select r.rental_date, f.title from rental r
-- join inventory i on i.inventory_id = r.inventory_id
-- join film f on f.film_id = i.film_id
-- where r.customer_id = 5;

-- 정답
-- SELECT r.rental_date, f.title
-- FROM rental r
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE r.customer_id = 5;

-- 4번 문제
-- 내가 푼 방법
-- select title from film order by release_year desc limit 10;
-- 정답
-- SELECT title
-- FROM film
-- ORDER BY release_year DESC
-- LIMIT 10;

-- 조인 및 관계
-- 1번 문제
-- 내가 푼 방법
-- select concat(a.first_name, ' ', a.last_name) as full_name
-- from actor a
-- join film_actor fa on fa.actor_id = a.actor_id
-- join film f on f.film_id = fa.film_id
-- where f.title = 'ACADEMY DINOSAUR'; 

-- 정답
-- SELECT a.first_name, a.last_name
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- JOIN film f ON fa.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- 2번 문제
-- 내가 푼 방법
-- select concat(c.first_name, ' ', c.last_name) as full_name
-- from customer c
-- join rental r on r.customer_id = c.customer_id
-- join inventory i on i.inventory_id = r.inventory_id
-- join film f on f.film_id = i.film_id
-- where f.title = 'ACADEMY DINOSAUR';

-- 정답
-- SELECT DISTINCT c.first_name, c.last_name
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- WHERE f.title = 'ACADEMY DINOSAUR';

-- 3번 문제
-- 내가 푼 방법
-- select c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
-- from customer c
-- join rental r on r.customer_id = c.customer_id
-- join inventory i on i.inventory_id = r.inventory_id
-- join film f on f.film_id = i.film_id
-- group by c.first_name, c.last_name, f.title;

-- 정답
-- SELECT c.customer_id, c.first_name, c.last_name, MAX(r.rental_date) as last_rental_date, f.title
-- FROM customer c
-- JOIN rental r ON c.customer_id = r.customer_id
-- JOIN inventory i ON r.inventory_id = i.inventory_id
-- JOIN film f ON i.film_id = f.film_id
-- GROUP BY c.customer_id, c.first_name, c.last_name, f.title;

-- 4번 문제
-- 내가 푼 방법
-- select f.title, avg(datediff(r.return_date, r.rental_date)) as avg_rental_date
-- from rental r
-- join inventory i on i.inventory_id = r.inventory_id
-- join film f on f.film_id = i.film_id
-- group by f.title;

-- 정답
-- SELECT f.title, AVG(DATEDIFF(r.return_date, r.rental_date)) as avg_rental_period
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title;

-- 집계 및 그룹화
-- 1번 문제
-- 내가 푼 방법
-- select f.title, count(r.inventory_id) as rental_count
-- from rental r
-- join inventory i on i.inventory_id = r.inventory_id
-- join film f on f.film_id = i.film_id
-- group by f.title
-- order by rental_count desc
-- limit 1;

-- 정답
-- SELECT f.title, COUNT(r.rental_id) as rental_count
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- GROUP BY f.title
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- 2번 문제
-- 내가 푼 방법
-- select c.name, avg(f.rental_rate) as avg_rental_rate
-- from category c
-- join film_category fc on fc.category_id = c.category_id
-- join film f on f.film_id = fc.film_id
-- group by c.name;

-- 정답
-- SELECT c.name, AVG(f.rental_rate) as average_rental_rate
-- FROM category c
-- JOIN film_category fc ON c.category_id = fc.category_id
-- JOIN film f ON fc.film_id = f.film_id
-- GROUP BY c.name;

-- 3번 문제
-- 내가 푼 방법
-- select year(payment_date) as year, month(payment_date) as month, sum(amount) as total_amount 
-- from payment
-- group by month, year;

-- 정답
-- SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales
-- FROM payment p
-- GROUP BY YEAR(p.payment_date), MONTH(p.payment_date);

-- 4번 문제
-- 내가 푼 방법
-- select a.actor_id, concat(a.first_name, ' ', a.last_name) as full_name, count(fa.film_id) as count_film
-- -- select a.actor_id, a.first_name, a.last_name, count(fa.film_id) as count_film
-- from actor a
-- join film_actor fa on fa.actor_id = a.actor_id
-- group by a.actor_id, a.first_name, a.last_name;

-- 정답
-- SELECT a.first_name, a.last_name, COUNT(fa.film_id) as number_of_films
-- FROM actor a
-- JOIN film_actor fa ON a.actor_id = fa.actor_id
-- GROUP BY a.first_name, a.last_name;

-- 서브쿼리 및 고급 기능
-- 1번 문제
-- 내가 푼 방법
-- select f.title, sum(p.amount) as total_amount
-- from film f
-- join inventory i on i.film_id = f.film_id
-- join rental r on r.inventory_id = i.inventory_id
-- join payment p on r.rental_id = p.rental_id
-- group by f.title
-- order by total_amount desc
-- limit 1;

-- 정답
-- SELECT f.title, SUM(p.amount) AS total_revenue
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- GROUP BY f.title
-- ORDER BY total_revenue DESC
-- LIMIT 1;

-- 2번 문제
-- 내가 푼 방법
-- select title, rental_rate from film
-- where rental_rate > (select avg(rental_rate) from film);

-- 정답
-- SELECT f.title, f.rental_rate
-- FROM film f
-- WHERE f.rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 3번 문제
-- 내가 푼 방법
-- select concat(c.first_name, ' ', c.last_name) as full_name, count(r.customer_id) as rental_count
-- from customer c
-- join rental r on r.customer_id = c.customer_id
-- group by c.first_name, c.last_name
-- order by rental_count desc
-- limit 1;

-- 정답
-- SELECT c.customer_id, c.first_name, c.last_name, COUNT(r.rental_id) AS rental_count
-- FROM rental r
-- JOIN customer c ON r.customer_id = c.customer_id
-- GROUP BY c.customer_id
-- ORDER BY rental_count DESC
-- LIMIT 1;

-- 4번 문제
-- 내가 푼 방법
-- select concat(a.first_name, ' ', a.last_name) as actor_full_name, f.title, count(r.inventory_id) as count_rental_film
-- from actor a
-- join film_actor fa on fa.actor_id = a.actor_id
-- join film f on f.film_id = fa.film_id
-- join inventory i on i.film_id = f.film_id
-- join rental r on r.inventory_id = i.inventory_id
-- where a.first_name = 'PENELOPE' and a.last_name = 'GUINESS'
-- group by a.first_name, a.last_name, f.title
-- order by count_rental_film desc
-- limit 1;

-- 정답
-- SELECT f.title, COUNT(r.rental_id) AS rental_count
-- FROM film f
-- JOIN film_actor fa ON f.film_id = fa.film_id
-- JOIN actor a ON fa.actor_id = a.actor_id
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- WHERE a.first_name = 'PENELOPE' AND a.last_name = 'GUINESS'
-- GROUP BY f.title
-- ORDER BY rental_count DESC
-- LIMIT 1;

