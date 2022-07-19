####################################################################################################
## Script Details                                                                                 ##
####################################################################################################
#                                                                                                 ##
# File            : market.py                                                                     ##
# Author          : Varun Pius Rodrigues                                                          ##
# Description     : Main program for the online market web application                            ##
#                                                                                                 ##
####################################################################################################
# Change Log:                                                                                     ##
# Date        Author                Description                                                   ##
####################################################################################################
#                                                                                                 ##
# 2022-07-18  Varun Pius Rodrigues  XXXX: Base application                                        ##
#                                                                                                 ##
####################################################################################################
# TODO:
# //TODO: Flask configuartion in separate file: 
#           https://haseebmajid.dev/blog/simple-app-flask-sqlalchemy-and-docker
# //TODO: DB user creation and access grant
#           https://georgexyz.com/run-mysql-in-a-docker-container-with-flask.html
#           https://stackoverflow.com/questions/46478714/mysql-docker-container-grant-user-privileges-warning
#           https://liman.io/blog/migration-dockerized-mysql-sqlalchemy-alembic
#
# //CHECK: https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa
#          https://www.stefanproell.at/tags/docker-compose.-grant/
####################################################################################################


####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# Standard Modules:
import os
from pathlib import Path

# External modules:
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Internal modules:
#import models
#import routes

####################################################################################################
# Configuration and Variable Setting                                                              ##
####################################################################################################

# Directory Config #
#template_dir = os.path.abspath('../templates')
template_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'templates')
dotenv_path = Path('properties/application.env')
load_dotenv(dotenv_path=dotenv_path)

# Database variables Config #
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
root_user = 'root'
root_pwd = 'root' #os.getenv('MYSQL_ROOT_PASSWORD')
host = 'host.docker.internal' #os.getenv('MYSQL_HOST')
port = '3306' #os.getenv('MYSQL_PORT')
database = 'market' #os.getenv('MYSQL_DATABASE')
#DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
DATABASE_CONNECTION_URI = f'mysql+pymysql://{root_user}:{root_pwd}@{host}:{port}/{database}'
#DATABASE_CONNECTION_URI = 'sqlite:///market.db'

# Flask Config #
# the app is used as decorator. eg: @app.route
app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


####################################################################################################
# Code start                                                                                      ##
####################################################################################################

# Database object model ##
class Item(db.Model):
    idx = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=True)

    def __repr__(self):
        return f'Item {self.name}\'s price is {self.price}'


# Home page
@app.route("/")
@app.route("/home")
def home_page():
    #return "<p>Marketplace Home Page!</p>".format(__name__)
    return render_template('home.html')

# Profile Page
@app.route("/profile/<user>")
def profile_page(user):
    return "<p>Hello {}</p>".format(user)

# Market page
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
    #items = [
    #    {'id': 1, 'name': 'iPhone', 'code': 'A123QR', 'price': 1000},
    #    {'id': 2, 'name': 'Laptop', 'code': 'A124QD', 'price': 1500},
    #    {'id': 3, 'name': 'Camera', 'code': 'b325rQ', 'price': 600},
    #    {'id': 4, 'name': 'Watch', 'code': 'c486xZ', 'price': 400}
    #]
    # data sent here to template via Jinja Templates
    #return render_template('market.html', item_name="iPhone")


####################################################################################################
# Code End                                                                                        ##
####################################################################################################
