SELECT c.city, b.total_amount
FROM clients c
JOIN bookings b ON c.client_id = b.client_id
JOIN cars r ON b.car_id = r.car_id
WHERE b.start_date >= '2020-07-12'

AND r.horse_power <= 300
ORDER BY c.city DESC;


SELECT c.city, b.total_amount
FROM clients c
JOIN bookings b ON c.client_id = b.client_id
JOIN cars r ON b.car_id = r.car_id
WHERE b.start_date >= '2020-07-12'

AND r.horse_power <= 300
ORDER BY c.city DESC

