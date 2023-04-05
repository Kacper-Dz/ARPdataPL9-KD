## Zadanie 1
## Utwórz tabele "Produkt" 
## z identyfiaktorem "id" integer,
## "Nazwa" o typie varchar - długośc 20 
## "Producent" o typie varchar - dlugość 20
## "Sekretariat" o typie varchar - dlugosc 20
## dodaj not null atrybut dla kolumny "nazwa"
## dla kolumny id dodaj "AUTO_INCREMENT"

CREATE TABLE sakila.Produkt
(
 id INTEGER not null UNIQUE, ##  not null and unique
 id_key integer not null,
 Nazwa VARCHAR(20) NOT NULL,
 Producent VARCHAR(25) NOT NULL,
 Sekretariat VARCHAR(25),
 PRIMARY KEY (ID) ## primary key
);


## Po wykonaniu prawym klawiszem myszy kliknij w schemat sakila i wybierz opcje Refresh ALL
## pokazać auto_incremant https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html

## następnie za pomoca funkcji ALTER usun kolumne "Sekretariat"
ALTER TABLE sakila.Produkt
  DROP COLUMN Sekretariat;
  
## następnie za pomoca funkcji ALTER dodaj kolumne "Opiekun"
ALTER TABLE sakila.Produkt
ADD Opiekun VARCHAR(255)
AFTER Producent;

## następnie za pomoca funkcji ALTER zmodyfikujmy kolumne "Opiekun"
ALTER TABLE sakila.Produkt
  MODIFY Opiekun varchar(50) NULL;
  
  
CREATE TABLE sakila.animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) DEFAULT 'Anonim', ## czy tu może być null
     PRIMARY KEY (id)
);
## pokazać auto_incremant https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html

INSERT INTO sakila.animals (id,name) VALUES(100,'rabbit');
INSERT INTO sakila.animals (id,name) VALUES(NULL,'mouse');
INSERT INTO sakila.animals (id) VALUES(103); ## czy tu możecie wpisac numer niższy niż w auto_increment
SELECT * FROM sakila.animals;

## wprowadz klucz obcy na id 
ALTER TABLE sakila.Produkt ADD CONSTRAINT id_key FOREIGN KEY (id_key) REFERENCES produkt(id);

## usuńmy klucz główny ## 
ALTER TABLE sakila.Produkt DROP FOREIGN KEY id_key;


## insert 
select * from sakila.Produkt;

INSERT INTO sakila.Produkt (Nazwa, Producent, Opiekun)
VALUES (1, 'Acer', 'Jan Nowak');

select * from sakila.Produkt;

## następnie usun tabele "Produkt" przez funkcje drop 
drop table sakila.Produkt;

## tworzenie tabeli z automatycznym wypełnieniem klucza
CREATE TABLE sakila.Produkt
(
 id MEDIUMINT, # NOT NULL AUTO_INCREMENT,
 Nazwa VARCHAR(20),
 Producent VARCHAR(25),
 Opiekun VARCHAR(25)

) ;

## insert
INSERT INTO sakila.Produkt (Nazwa, Producent, Opiekun)
VALUES ('Laptopy', 'Acer', 'Jan Nowak');

INSERT INTO sakila.Produkt (id, Nazwa, Producent, Opiekun)
VALUES (1, 'Laptopy', 'Acer', 'Jan Nowak');


## spróbujcie zmodyfikowac tabele - nie dziala ?
## https://sebhastian.com/mysql-error-code-1175/
SET SQL_SAFE_UPDATES = 0;

## udpate
UPDATE sakila.Produkt 
SET Producent='Asus' 
WHERE Nazwa='Laptopy';

UPDATE sakila.Produkt     
SET Producent = 'Asus'    
WHERE Nazwa = 'Laptopy';  
 ## sprawdzić

## udpate
DELETE FROM sakila.Produkt  
WHERE Nazwa='Laptopy'; ## sprawdzić
