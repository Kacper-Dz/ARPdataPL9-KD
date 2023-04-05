## Agregacja
select 	count(*) 
from 	sakila.inventory;


SELECT  	avg(rental_rate)
FROM 		sakila.film;

SELECT  	min(rental_rate)
FROM 		sakila.film;

SELECT  	max(rental_rate)
FROM 		sakila.film;

SELECT  	min(rental_rate), avg(rental_rate), max(rental_rate)
FROM 		sakila.film
where 		release_year ='2006';

select 		*
from  		sakila.payment;

select 		staff_id, avg(amount), min(amount), max(amount) 
from 		sakila.payment
group by 	staff_id;

select 		staff_id, min(payment_date), max(payment_date) 
from 		sakila.payment
group by 	staff_id;

select 		staff_id, avg(amount), sum(amount)
from 		sakila.payment
where 		payment_date > '2005-07-23 00:00:00'
group by 	staff_id;

drop table sakila.Produkt;

-- Zadanie 10
-- 1. Wypisz wszystkie samochody, których rok produkcji jest większy niż 2015.

SELECT  	*
FROM 		car_rental.cars
where 		year > '2015';

-- 2. *Wypisz wszystkie rezerwacje, których koszt całkowity znajduje się w
-- przedziale 1000-2555.total_amount

SELECT  	*
FROM 		car_rental.bookings
where 		total_amount < '2555' AND total_amount > '1000';

-- 3. *Wypisz id wszystkich klientów, których nazwisko zaczyna się na literę 'N'
-- oraz imię kończy się na litery 'ej'.

SELECT  	client_id
FROM 		car_rental.clients
WHERE surname LIKE 'N%' AND name LIKE '%ej'; # LIKE 'N%' - wpis musi byc jako "n%' - czyli pierwszy znak to N a % reprezentuje reszte wartości, 'H%J' - bedziemy szukac wartosci zaczynajacych sie na H i konczacych sie na J

