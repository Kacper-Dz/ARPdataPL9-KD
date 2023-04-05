## Stwórz tabelę Produkt w bazie sakila: sakila.Produkt
## "Nazwa" o typie varchar - długosć 20
## "Producent" o typie varchar - długosć 20
## "Sekretariat" o typie varchar - dlugosc 20
## dodaj not null atrybuty dla kolumny "nazwa" - not null oznacza, że komórka nie może posiadać pustej wartości
## dla kolumny id dodaj "AUTO_INCREMENT"
drop table sakila.Produkt;

CREATE TABLE sakila.Produkt
(
 id INTEGER not null UNIQUE, ##  not null and unique
 id_key integer not null,
 Nazwa VARCHAR(20) NOT NULL,
 Producent VARCHAR(25) NOT NULL,
 Sekretariat VARCHAR(25),
 PRIMARY KEY (ID) ## primary key
);

select * from sakila.Produkt;

## usuwanie kolumny sekretariat
ALTER TABLE sakila.Produkt
  DROP COLUMN Sekretariat;
  
select * from sakila.Produkt;

## Dodanie kolumny opiekun
ALTER TABLE sakila.Produkt
ADD Opiekun VARCHAR(255)  # Wartość w nawiasie oznacza limit ilości znaków
AFTER Producent;

select * from sakila.Produkt;

## Modyfikujemy kolumnę 
ALTER TABLE sakila.Produkt
MODIFY Opiekun VARCHAR(50) NULL;

drop table sakila.animals;
## pokazać auto_incremant https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html
CREATE TABLE sakila.animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) DEFAULT 'Anonim', ## czy tu może być null
     PRIMARY KEY (id)
);
select * from sakila.animals;
INSERT INTO sakila.animals (id,name) VALUES(100,'rabbit');  # Dodajemy do sakila.animals wpis rabbit o id 100
INSERT INTO sakila.animals (id,name) VALUES(null,'mouse'); # Pomimo, że nie podaliśmy ID - został nadany automatycznie numer następny: autoincreament
INSERT INTO sakila.animals (id,name) VALUES(null,null);
INSERT INTO sakila.animals (id,name) VALUES(103);

drop table  sakila.Produkt;

CREATE TABLE sakila.Produkt
(
 id MEDIUMINT, # NOT NULL AUTO_INCREMENT,
 Nazwa VARCHAR(20),
 Producent VARCHAR(25),
 Opiekun VARCHAR(25)

) ;

INSERT INTO sakila.Produkt (Nazwa, Producent, Opiekun)
VALUES ('Laptopy', 'Acer', 'Jan Nowak');

INSERT INTO sakila.Produkt (id, Nazwa, Producent, Opiekun)
VALUES (1, 'Laptopy', 'Acer', 'Jan Nowak');

select * from sakila.Produkt;

SET SQL_SAFE_UPDATES = 0; # Wylacza zabezpieczenie tabeli

UPDATE sakila.Produkt 
SET Producent='Asus' 
WHERE Nazwa='Laptopy';

## delete
DELETE FROM sakila.Produkt  
WHERE Nazwa='Laptopy'; ## sprawdzić, usuwamy wszystko co ma w nazwie Laptopy