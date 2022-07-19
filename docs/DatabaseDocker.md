# Creating users with permissions
## SQL file
We create a SQL script with the queries that GRANT permissions to our users
```
privileges.sql

CREATE USER 'vpiusr'@'%' IDENTIFIED BY 'vpiusr';
GRANT ALL PRIVILEGES ON *.* TO 'vpiusr'@'%';
FLUSH PRIVILEGES;
```

This SQL script needs to be copied to the folder `/docker-entrypoint-initdb.d/` inside a Docker image. All SQL files inside /docker-entrypoint-initdb.d/ the directory would be executed by default when MySQL container boots. 

If we have `--skip-name-resolve` mode, MySQL does not consider the DNS lookup values and look for IP address which is default `127.0.0.1`. In this case, we would need to manually state the IP address as `-p 127.0.0.1:3306:3306` in the `docker run` command.

For the generic purpose, I have used `%` for any valid host. You can state the specific host here.


## Dockerfile
Next we start with the Dockerfile. Let's name our Dockerfile `Dockerfile-mysql`. It will be as follows:
```
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD root
COPY ./schemapath/privileges.sql /docker-entrypoint-initdb.d/
```

## Building the image
Finally, execute below docker comments to create a custom MySQL image and run it as a container in detached mode.
```
docker build -t custom-mysql . --file ./Dockerfile-mysql
docker run -d --name custom-mysql-container -p 127.0.0.1:3306:3306 custom-mysql
```

## Docker Compose
Test

## Validation
We could validate the above commands using the following steps:
```
docker ps -a
docker exec -it <containerID> mysql -uroot -proot

mysql> show grants for 'vpiusr';
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grants for vpiusr@%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `vpiusr`@`%`                                                                                                                                                                                                                                                                                                                                                 |
| GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SENSITIVE_VARIABLES_OBSERVER,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `vpiusr`@`%` |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
*/
```

# Python SQLAlchemy
## Creating table of the model:
```
from market import db
db.create_all()
from market import Item
item1 = Item(name = 'iPhone 10', price = 500, barcode = '123qdw', description = 'Latest iphone, mint condition')
item2 = Item(name = 'iMac', price = 1200, barcode = 'lap564x', description = 'New iMac, 27 inches')
item3 = Item(name = 'Apple Watch', price = 300, barcode = 'acce6x', description = 'Apple watch 6 - 44mm')
db.session.add(item1)
db.session.add(item2)
db.session.commit()
Item.query.all()
```

## Accessing data:
Everytime a change is made in the main codebase, we won't be able to access it in this session except for the data. So for that, we exit and start new session:
```
from market import db
from market import Item
Item.query.all()

for item in Item.query.all():
    item.name
    item.price

Item.query.filter_by(price=500)     # this will return Item object; to access value try the next step
for item in Item.query.filter_by(price=500):
    item.name
    item.price

```

# Accessing Docker image
When the docker images are created using Docker Compose, we use `links` in the services using the database container. This let's us access the container from other services using the db service name (that's set in the Docker Compose file). However, if you don't do that, we can access the database container as though it's a native database instance running on native host system. Accessing native hosted system can be done by setting the `HOST` value of database as `'host.docker.internal'`