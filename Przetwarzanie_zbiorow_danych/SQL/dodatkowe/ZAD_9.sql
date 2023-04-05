INSERT INTO clients (name, surname, address, city)
VALUES
('Jan', 'Kowalski', 'ul. Florianska 12', 'Krakow'),
('Andrzej', 'Nowak', 'ul. Saska 43', 'Wroclaw' );


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