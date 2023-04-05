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
 
-- Zadanie 10
-- 1. Wypisz wszystkie samochody, których rok produkcji jest większy niż 2015.
-- 2. *Wypisz wszystkie rezerwacje, których koszt całkowity znajduje się w
-- przedziale 1000-2555.
-- 3. *Wypisz id wszystkich klientów, których nazwisko zaczyna się na literę 'N'
-- oraz imię kończy się na litery 'ej'.
 
#1)
SELECT *
FROM cars
WHERE year > 2015;
#2)
SELECT *
FROM bookings
WHERE total_amount
BETWEEN 1000 AND 2555;
#3)
SELECT client_id
FROM clients
WHERE surname
LIKE "N%" AND name LIKE "%ej";