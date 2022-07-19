import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('properties/application.env')
load_dotenv(dotenv_path=dotenv_path)

user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
root_pwd = os.getenv('MYSQL_ROOT_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('MYSQL_DATABASE')

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

print(user, password, root_pwd, host, port, database)