####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# Standard Modules:
import os

# External modules:
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


####################################################################################################
# Configurations                                                                                  ##
####################################################################################################

## Directory Config ##
#template_dir = os.path.abspath('../templates')
#template_dir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
template_dir = os.path.join(basedir, 'templates')
database_dir = os.path.join(basedir, 'src', 'properties', 'market.db')
dotenv_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
dotenv_path = os.path.join(template_dir, 'properties', 'application.env')
load_dotenv(dotenv_path=dotenv_path)


## Database Config ##
user      = os.getenv('MYSQL_USER')
password  = os.getenv('MYSQL_PASSWORD')
root_user = 'root'
root_pwd  = 'root'                      #os.getenv('MYSQL_ROOT_PASSWORD')
host      = 'db'                        #os.getenv('MYSQL_HOST')
port      = '3306'                      #os.getenv('MYSQL_PORT')
database  = 'market'                    #os.getenv('MYSQL_DATABASE')
DATABASE_CONNECTION_URI = f'mysql+pymysql://{root_user}:{root_pwd}@{host}:{port}/{database}'

#DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
#DATABASE_CONNECTION_URI = 'sqlite:///market.db'    #if db in same location
#DATABASE_CONNECTION_URI = 'sqlite:///' + database_dir


## Flask Config ##
# the app is used as decorator. eg: @app.route
app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


####################################################################################################
# All circular imports here:                                                                      ##
####################################################################################################
'''
Circular imports are once where file1 is importing from file2 and file 2 is importing from file1.
To resolve this, ordering is important.

If we dont include `from market import routes` then `__init__.py` file will start the Flask app but it won't know how to redirect/route URLs. So we need to import `routes`. 
However, `routes` itself is dependent on `app` from `__init__`. 

So we first create the `app` and then we import `routes` at which time `routes` itself would have access to app and can run successfully
'''
from market import routes
