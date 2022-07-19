docker build -t custom-mysql . --file ./Dockerfile-mysql
docker run -d --name custom-mysql-container -p 3306:3306 custom-mysql
docker exec -it d9269ca25c35 mysql -uroot -p

docker exec -i d219267acd4e bash -c "cd /code/src && ls -la"
docker exec -it 4905d22ceeec bash -c "cd /code/src && python"
docker exec -i 6258f33dfb3d bash -c "cd /docker-entrypoint-initdb.d && ls -la"


from market import db
db.create_all()
from market import Item
item1 = Item(name = 'iPhone 10', price = 500, code = '123qdw', description = 'Latest iphone, mint condition')
db.session.add(item1)
db.session.commit()
Item.query.all()

for item in Item.query.all():
    item.name
    item.price
