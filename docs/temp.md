docker build -t custom-mysql . --file ./Dockerfile-mysql
docker run -d --name custom-mysql-container -p 3306:3306 custom-mysql
docker exec -it d9269ca25c35 mysql -uroot -p

docker exec -i d219267acd4e bash -c "cd /code/src && ls -la"
docker exec -it c6886340bb47 bash -c "cd /code/src && python"
docker exec -i 6258f33dfb3d bash -c "cd /docker-entrypoint-initdb.d && ls -la"

docker exec -i 9fec96431a54 bash -c "cd /code/src/market && ls -la"

from market import db
db.create_all()
from market import Item
from market.models import Item
item1 = Item(name = 'iPhone 10', price = 500, code = '123qdw', description = 'Latest iphone, mint condition')
db.session.add(item1)
db.session.commit()
Item.query.all()

for item in Item.query.all():
    item.name
    item.price



---------------------------------------------------------------------------------------------


```
app = Flask(__name__, template_folder="public/ui/build/", static_folder=os.path.join(CWD, "public/ui/build/static/"), static_url_path="/static")
```

If you just want to move the location of your static files, then the simplest method is to declare the paths in the constructor. In the example below, I have moved my templates and static files into a sub-folder called web.

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

    static_url_path='' removes any preceding path from the URL (i.e. the default /static).
    static_folder='web/static' to serve any files found in the folder web/static as static files.
    template_folder='web/templates' similarly, this changes the templates folder.

https://newbedev.com/how-to-serve-static-files-in-flask

