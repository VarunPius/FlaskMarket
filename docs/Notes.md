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
### Fask(name)
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
