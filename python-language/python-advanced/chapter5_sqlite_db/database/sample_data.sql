/* http://random-name-generator.info
   Author: Mahmud Ahsan
   Twitter: @mahmudahsan
*/

/* Clearing Existing Data | Inserting New Data */

DELETE FROM addresses;
DELETE FROM users;

INSERT INTO users(first_name, last_name) VALUES ('Ernesto','Fuller');
INSERT INTO users(first_name, last_name) VALUES ('Cedric','Moreno');
INSERT INTO users(first_name, last_name) VALUES ('Terrence','Jordan');
INSERT INTO users(first_name, last_name) VALUES ('Lionel','Medina');
INSERT INTO users(first_name, last_name) VALUES ('Kristy','Hicks');


INSERT INTO addresses(user_id, email, address) VALUES (1, 'erfu@gmail.com',  'BD');
INSERT INTO addresses(user_id, email, address) VALUES (2, 'cedmo@gmail.com', 'US');
INSERT INTO addresses(user_id, email, address) VALUES (3, 'terjor@msn.com',  'CA');
INSERT INTO addresses(user_id, email, address) VALUES (4, 'lime@yahoo.com',  'IN');
INSERT INTO addresses(user_id, email, address) VALUES (5, 'krhi@bbc.com',    'DN');

/* Sample Query */
SELECT first_name, last_name FROM users WHERE last_name LIKE 'M%';

/* Joining Query */
SELECT u.last_name as last_name,
       a.email as email, a.address as address
FROM users AS u
LEFT JOIN addresses as a
WHERE u.id=a.user_id AND u.last_name LIKE 'M%';



