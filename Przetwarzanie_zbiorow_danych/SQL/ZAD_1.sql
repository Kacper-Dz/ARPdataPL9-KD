-- Zadanie 10
-- 1. TABELA CARS Wypisz wszystkie samochody, których rok produkcji jest większy niż 2015.
-- 2. TABELA BOOKINGS Wypisz wszystkie rezerwacje, których koszt całkowity znajduje się w
-- przedziale 1000-2555.
-- 3. TABELA CLIENTS Wypisz id wszystkich klientów, których nazwisko zaczyna się na literę 'N'
-- oraz imię kończy się na litery 'ej'.
CREATE  DATABASE car_rental;

USE car_rental;


CREATE TABLE cars
(
 car_id INTEGER PRIMARY KEY,
 producer VARCHAR(30),
 model VARCHAR(30),
 year INTEGER,
 horse_power INTEGER,
 price_per_day INTEGER
);
CREATE TABLE clients
(
 client_id INTEGER PRIMARY KEY,
 name VARCHAR(30),
 surname VARCHAR(30),
 address TEXT,
 city VARCHAR(30)
);
CREATE TABLE bookings
(
 booking_id INTEGER PRIMARY KEY,
 client_id INTEGER,
 car_id INTEGER,
 start_date DATE,
 end_date DATE,
 total_amount INTEGER
);

INSERT INTO clients (name, surname, address, city)
VALUES
('Paweł', 'Kowalski', 'ul. Florianska 12', 'Krakow'),
('Gaweł', 'Nowak', 'ul. Saska 43', 'Wroclaw' );


INSERT INTO cars (producer, model, year, horse_power,
price_per_day)
VALUES
('Seat', 'Leon', 2016, 80, 200),
('Toyota', 'Avensis', 2014, 72, 100);


INSERT INTO bookings (client_id, car_id, start_date, end_date,
total_amount)
VALUES
(1, 2, '2020-07-05', '2020-07-06', 100),
(2, 2, '2020-07-10', '2020-07-12', 200);


INSERT INTO clients (name, surname, address, city)
VALUES
 ('Michal', 'Taki', 'os. Srodkowe 12', 'Poznan'),
 ('Pawel', 'Ktory', 'ul. Stara 11', 'Gdynia'),
 ('Anna', 'Inna', 'os. Srednie 1', 'Gniezno'),
 ('Alicja', 'Panna', 'os. Duze 33', 'Torun'),
 ('Damian', 'Papa', 'ul. Skosna 66', 'Warszawa'),
 ('Marek', 'Troska', 'os. Male 90', 'Radom'),
 ('Jakub', 'Klos', 'os. Polskie 19', 'Wadowice'),
 ('Lukasz', 'Lis', 'os. Podlaskie 90', 'Bialystok');
 
INSERT INTO cars (producer, model, year, horse_power,
price_per_day) VALUES
 ('Mercedes', 'CLK', 2018, 190, 400),
 ('Hyundai', 'Coupe', 2014, 165, 300),
 ('Dacia', 'Logan', 2015, 103, 150),
 ('Saab', '95', 2012, 140, 140),
 ('BMW', 'E36', 2007, 110, 80),
 ('Fiat', 'Panda', 2016, 77, 190),
 ('Honda', 'Civic', 2019, 130, 360),
 ('Volvo', 'XC70', 2013, 180, 280);
 
INSERT INTO bookings (client_id, car_id, start_date,
end_date, total_amount) VALUES
 (3, 3, '2020-07-06', '2020-07-08', 400),
 (6, 10, '2020-07-10', '2020-07-16', 1680),
 (4, 5, '2020-07-11', '2020-07-14', 450),
 (5, 4, '2020-07-11', '2020-07-13', 600),
 (7, 3, '2020-07-12', '2020-07-14', 800),
 (5, 7, '2020-07-14', '2020-07-17', 240),
 (3, 8, '2020-07-14', '2020-07-16', 380),
 (5, 9, '2020-07-15', '2020-07-18', 1080),
 (6, 10, '2020-07-16', '2020-07-20', 1120),
 (8, 1, '2020-07-16', '2020-07-19', 600),
 (9, 2, '2020-07-16', '2020-07-21', 500),
 (10, 6, '2020-07-17', '2020-07-19', 280),
 (1, 9, '2020-07-17', '2020-07-19', 720),
 (3, 7, '2020-07-18', '2020-07-21', 240),
 (5, 4, '2020-07-18', '2020-07-22', 1200);
 

ALTER TABLE clients MODIFY COLUMN client_id INTEGER
AUTO_INCREMENT;
ALTER TABLE cars MODIFY COLUMN car_id INTEGER
AUTO_INCREMENT;
ALTER TABLE bookings MODIFY COLUMN booking_id INTEGER
AUTO_INCREMENT;

select  	model, 
			sum(full_price)
from 		(
			select 			crc.model,  
							crc.price_per_day * (crb.end_date - crb.start_date) as full_price
			from 			car_rental.bookings as crb
			left join 		car_rental.cars as crc
			on 				crb.car_id = crc.car_id) as tab
group by model;