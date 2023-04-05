

#1)
SELECT c.name, b.total_amount
FROM bookings b
JOIN clients c ON c.client_id = b.client_id
WHERE b.total_amount > 1000;
#2)
SELECT c.city, b.total_amount
FROM clients c
JOIN bookings b ON c.client_id = b.client_id
JOIN cars r ON b.car_id = r.car_id
WHERE b.start_date >= '2020-07-12'
AND b.end_date <= '2020-07-20'
AND r.horse_power <= 120
ORDER BY b.total_amount DESC;
#3)
SELECT COUNT(b.car_id)
FROM bookings b
JOIN cars r ON b.car_id = r.car_id
WHERE r.price_per_day >= 300
GROUP BY r.horse_power
ORDER BY r.horse_power;
#4)
SELECT SUM(total_amount)
FROM bookings
WHERE start_date >= '2020-07-14'
AND end_date <= '2020-07-18';
#5)
SELECT AVG(b.total_amount) AS
Srednia_wartosc_rezerwacji,
COUNT(b.car_id) AS
Liczba_wypozyczonych_samochodow,
c.name AS Imie, c.surname AS Nazwisko
FROM bookings b
JOIN clients c ON c.client_id = b.client_id
GROUP BY b.client_id
HAVING Liczba_wypozyczonych_samochodow >= 2
ORDER BY Liczba_wypozyczonych_samochodow DESC; 