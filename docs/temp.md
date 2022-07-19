docker build -t custom-mysql . --file ./Dockerfile-mysql
docker run -d --name custom-mysql-container -p 3306:3306 custom-mysql
docker exec -it d9269ca25c35 mysql -uroot -p

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
