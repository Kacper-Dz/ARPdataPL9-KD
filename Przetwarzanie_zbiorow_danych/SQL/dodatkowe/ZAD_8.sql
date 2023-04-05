DROP DATABASE car_rental;
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

ALTER TABLE clients MODIFY COLUMN client_id INTEGER
AUTO_INCREMENT;
ALTER TABLE cars MODIFY COLUMN car_id INTEGER
AUTO_INCREMENT;
ALTER TABLE bookings MODIFY COLUMN booking_id INTEGER
AUTO_INCREMENT;

ALTER TABLE bookings
ADD CONSTRAINT client_id_fk FOREIGN KEY (client_id)
REFERENCES clients (client_id),
ADD CONSTRAINT car_id_fk FOREIGN KEY (car_id)
REFERENCES cars (car_id);