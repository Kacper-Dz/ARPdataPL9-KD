select * from sakila.film; ## Dostęp do tabeli

select title from sakila.film; ## Dostęp do kolumn
select * from sakila.film
limit 1; ## dostęp do wiersza (pamiętać o ; !!!!!!!!)

# Relacyjność
select film_id, title from sakila.film;

select film_id, actor_id from sakila.film_actor;

# komenda as aliasuje nam nazwy tabel

# Łączenie
select 		f.film_id,   # z tabeli f film_id
			f.title,     # z tabeli f title
            fa.actor_id  # z tabeli fa actor_id
from sakila.film as f
left join	sakila.film_actor as fa
on			f.film_id = fa.film_id
;
# Aliasujemy nazwy tabel aby skrócić długość zapytań (f i fa)

# Zliczanie ilosci wierszy w tabeli
select count(*) from sakila.film; ## 1000
select count(*) from sakila.film_actor; ## 5462

# To jest nasze zapytanie, ono zwraca wartosc na bazie tego co sie dzieje w podzapytaniu
select count(*) from
			(
			# To jest nasze podzapytanie
			select 		f.film_id,
						f.title,   
						fa.actor_id 
			from sakila.film as f
			left join	sakila.film_actor as fa
			on			f.film_id = fa.film_id
			) as tab;
            
INSERT INTO car_rental.clients (name, surname, address, city)
VALUES
('Paweł', 'Kowalski', 'ul. Florianska 12', 'Krakow'), # Nawias oznacza nowy wiersz
('Gaweł', 'Nowak', 'ul. Saska 43', 'Wroclaw' );

## Selecty
SELECT  	*
FROM 		sakila.film
WHERE 		length='86' AND              # where to jest warunek, tutaj filtrujemy po: 1) długości wpisu - 86 oraz 2) wyszukuje słowo 'epic' w kolemnie description 
			description LIKE '%epic%';
            
## Limity            
select 		*  
from 		sakila.film           
WHERE 		length <'86' 
LIMIT 		4;  
 
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

select		staff_id, avg(amount)
from		sakila.payment
group by 	staff_id;