DROP USER 'vpiusr'@'%';

FLUSH PRIVILEGES;


/* */
CREATE USER 'vpiusr'@'%' IDENTIFIED BY 'key4access';

/* */
GRANT ALL ON *.* TO 'vpiusr'@'%';

/* */
FLUSH PRIVILEGES;
