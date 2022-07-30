# Docker
## Shortcuts
Start Docker compose services:
```
docker-compose up -d
```

Stop Docker compose services:
```
docker-compose stop
```

Remove containers:
```
docker-compose down
```

## Lessons:
Accepted ways to write key value pairs:
```
environment:
  - FLASK_ENV=development
  - "FLASK_ENV:development"
  - FLASK_ENV:development
  FLASK_ENV: development
```

Following gives error:
- `[services.web.environment.0 must be a string]`: The extra space after `:` causes failure when it's a list (i.e it starts with `-`)
```
environment:
  - FLASK_ENV: development
```

# Flask
## Fundamentals
### Flask(name)
The variable `__name__` is passed as first argument when creating an instance of the Flask object (a Python Flask application). This would be one of the initial lines as follows:
```
app = Flask(__name__)
```

In this case `__name__` represents the name of the application package and it’s used by Flask to identify resources like templates, static assets and the instance folder. Try running this in our main program.

```
@app.route('/')
def example():
    return 'The value of __name__ is {}'.format(__name__)
```

In our case, the value would be `market`.

## Custom template and static folder values
By default, templates and static files are stored in the root folder under `templates` and `static`. However, if you change that, use the following parameters:
- `static_url_path=''` removes any preceding path from the URL (i.e. the default `/static`).
- `static_folder='web/static'` to serve any files found in the folder web/static as static files.
- `template_folder='web/templates'` similarly, this changes the templates folder.

Whatever we set the `static_url_path` to, under `routes` we need to set that same value for `@app.route`

For xxample, we set `static_url_path` to `/static`. Therefore, our route is set to `@app.route('/static/<path:filename>')`


## SECRET_KEY
When writing to database, we would need a secret key when dealing with forms.
Forms require the use of a secret key, which after verifying, will it write to database. 
So we generate the hex value in Python as follows:
```
>>> os.urandom(12).hex()
'1dedd39e59932fa82aca03e8'
```

This value is then added to the config:
```
app.config['SECRET_KEY'] = '1dedd39e59932fa82aca03e8'
```

## Flask-login
With Flask-login you need to use the following:
```
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
```
These lines are added in the Model. The reason we need to include these is because they provide session management.

When the user's credentials are taken, the session management such as whether the user is active or not active takes place via Flask-login, which takes `user_loader` to identify session.

Along with `load_user`, we need 4 more methods:
- `is_authenticated` : This property should return True if the user is authenticated, i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)
- `is_active` : This property should return True if this is an active user - in addition to being authenticated, they also have activated their account, not been suspended, or any condition your application has for rejecting an account. Inactive accounts may not log in (without being forced of course).
- `is_anonymous` : This property should return True if this is an anonymous user. (Actual users should return False instead.)
- `get_id()` : This method must return a str that uniquely identifies this user, and can be used to load the user from the user_loader callback. Note that this must be a str - if the ID is natively an int or some other type, you will need to convert it to str.

Instead of writing and defining these methods, we simply import and use `UserMixin`. `UserMixin` has these defined.

### login_view
Decorators are executed before the method/function is executed. So when we have `@app.route` before a method, the Flask application executes the route functionality before it creates and runs the specific method for which the decorator was applied (or route is intended to be created). Now, we want to protect some pages behind membership. In that case we use the decorator `@login_required` from `flask-login`. In our example, we want to restrict access to `market` page only to logged in users. So we apply `@login_required` to `market` route, and then we specify in `__init__` the following setting:
```
login_manager.login_view = 'login_page' 
```
This results in `market` page being redirected to `login` page and only after the user has logged in will the user be redirected back to `market` page. This is how the url will look:
``` 
http://localhost:8000/login?next=%2Fmarket
```