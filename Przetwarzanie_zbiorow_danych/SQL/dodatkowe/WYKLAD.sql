select * from sakila.film; ## dostęp do tabeli
select title from sakila.film; ## dostęp do kolumn
select * from sakila.film
limit 1; ## dostęp do wiersza


## Relacyjność
select film_id, title from sakila.film; 
select film_id, actor_id from sakila.film_actor;
select 		f.film_id,
			f.title,
			fa.actor_id
from 		sakila.film as f
left join 	sakila.film_actor fa
on 			f.film_id = fa.film_id; ## relacyjność pozwoliła nam połaczyć te tabele

select count(*) from sakila.film; ## 1000
select count(*) from sakila.film_actor; ## 1000 5462

select count(*) from 
(
select 	    f.film_id,
			f.title,
			fa.actor_id
from 		sakila.film f
left join 	sakila.film_actor fa
on 			f.film_id = fa.film_id
) AS some_name;

## Atomowość
select * from sakila.address; ## 603 mamy city ale nie mam country
select * from sakila.city; ## 600 mamy odniesienie do country

## Struktura danych
SHOW COLUMNS FROM sakila.city;

## Selecty
SELECT  	*
FROM 		sakila.film
WHERE 		length='86' AND 
			description LIKE '%epic%';
            
## Aliasy
SELECT  	title as Title
FROM 		sakila.film
WHERE 		length='86' AND 
			description LIKE '%epic%';            

## Limity            
select 		*  
from 		sakila.film           
WHERE 		length <'86' 
LIMIT 		4;  
 
## Agregacja
select 	count(*) 
from 	sakila.inventory;

## 4581
select 	* 
from 	sakila.inventory;

SELECT * FROM sakila.payment;

select 		avg(amount) 
from  		sakila.payment;

select 		staff_id, avg(amount) 
from 		sakila.payment
group by 	staff_id;

select 		staff_id, min(payment_date), max(payment_date)
from 		sakila.payment
group by 	staff_id;


select 		staff_id, avg(amount), sum(amount)
from 		sakila.payment
where 		payment_date > '2005-07-23 00:00:00'
group by 	staff_id;


HAVING COUNT(*) > 40
 

