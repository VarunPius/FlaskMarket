USE market;


/* Table: `item`
+-----+-------------+-------+---------+-------------------------------------------+-------+
| idx | name        | price | barcode | description                               | owner |
+-----+-------------+-------+---------+-------------------------------------------+-------+
|   1 | iPhone 10   |   500 | 123qdw  | Latest iphone, mint condition             |  NULL |
|   2 | iMac        |  1200 | lap564x | New iMac, 27 inches                       |     1 |
|   3 | Apple Watch |   300 | acce6x  | Apple watch 6 - 44mm                      |  NULL |
|   4 | PS4         |   350 | qwe784  | Original playstation 4 with 4 controllers |     2 |
+-----+-------------+-------+---------+-------------------------------------------+-------+
*/

INSERT INTO item
(name, price, barcode, description)
VALUES
("iPhone 13", 800, "mob001", "iPhone 13: Regular 6 inches with dual camera setup");

INSERT INTO item
(name, price, barcode, description, owner)
VALUES
("iMac", 2000, "pcx001", "iMac: 27 inches, 16 GB RAM, 256 GB SSD", 1);

INSERT INTO item
(name, price, barcode, description, owner)
VALUES
("Apple Watch 7", 349, "accq001", "Apple Watch 7: 44 mm smart watch with Health and tracking features", NULL);

INSERT INTO item
(name, price, barcode, description, owner)
VALUES
("PS4", 350, "funq01", "PlayStation 4: ", 2);

/* Table: `user`
+----+----------+-------------------+---------------+--------+
| id | username | email             | pwd_hash      | wallet |
+----+----------+-------------------+---------------+--------+
|  1 | vpiusr   | vpiusr@vpiusr.com | aQd34ert62855 |   5000 |
|  2 | vinu     | vinu@vpiusr.com   | aQerg4564e697 |     10 |
+----+----------+-------------------+---------------+--------+
*/

INSERT INTO user
(username, email, pwd_hash, wallet)
VALUES
("vpiusr", "vpiusr@vpiusr.com", "aQd34ert62855", 5000);

INSERT INTO user
(username, email, pwd_hash, wallet)
VALUES
("vinu", "vinu@vpiusr.com", "aQerg4564e697", 10);
