
--Noah Smith
--Bellevue University 
--12/16/23
--Final Project sql database creation
--version 2


CREATE DATABASE IF NOT EXISTS whatabook;
USE whatabook; 

-- deletes tables if they are already there, so there isn't any confusion 
DROP USER IF EXISTS 'whatabook_user'@'localhost';
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;



-- Checks if database is created
-- Then creates the database
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';
FLUSH PRIVILEGES;


-- Creates tables and links tables together with keys
CREATE TABLE user ( 
user_id	INT 	NOT NULL 	AUTO_INCREMENT,
first_name 	VARCHAR(75) 	NOT NULL,
last_name	VARCHAR(75) 	NOT NULL,
PRIMARY KEY (user_id)
);

CREATE TABLE book ( 
    book_id	INT 	NOT NULL 	AUTO_INCREMENT,
    book_name 	VARCHAR(200) 	NOT NULL,
    author	VARCHAR(200) 	NOT NULL,
    PRIMARY KEY (book_id)
);

CREATE TABLE store ( 
    store_id	INT 	NOT NULL,
    locale 	VARCHAR(500) 	NOT NULL,
    PRIMARY KEY (store_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY (wishlist_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);
-- Inserts info about store 
INSERT INTO store( store_id, locale) 
 VALUES ( '728', 'Jackson Street Books');
 
 -- Insert info about books
INSERT INTO book( book_id, book_name, author) 
 VALUES ( '501', 'Dune', 'Frank_Herbert');
INSERT INTO book( book_id, book_name, author) 
 VALUES ( '502', 'The Republic', 'Plato');
 INSERT INTO book( book_id, book_name, author) 
 VALUES ( '503', 'Bible OSB', 'Mark_Luke_John_Matt');
 INSERT INTO book( book_id, book_name, author) 
 VALUES ( '504', 'The_Fellowship_Of_The_Ring', 'JRR_Tolkien');
 INSERT INTO book( book_id, book_name, author) 
 VALUES ( '505', 'Out of the Silent Planet', 'C.S Lewis');
  INSERT INTO book( book_id, book_name, author) 
 VALUES ( '506', 'Windows10 For Dummies', 'Rathbone');
  INSERT INTO book( book_id, book_name, author) 
 VALUES ( '507', 'The Black Swan', 'Nassim Taleb');
  INSERT INTO book( book_id, book_name, author) 
 VALUES ( '508', 'Orthodoxy and the Religion of the Future', 'Seraphim Rose');
   INSERT INTO book( book_id, book_name, author) 
 VALUES ( '509', 'Learn Latin', 'Jones');


-- Inserts Users
INSERT INTO user( user_id, first_name, last_name) 
 VALUES ( '1', 'Noah', 'Smith');

INSERT INTO user( user_id, first_name, last_name) 
 VALUES ( '2', 'Saint', 'George');

 INSERT INTO user( user_id, first_name, last_name) 
 VALUES ( '3', 'Sarah', 'Prudence');
