from flask import Flask 
from host.config import Config
from flask_mysqldb import MySQL 

app = Flask(__name__,template_folder= '../app/templates', static_url_path = '',static_folder = '../app/static')
app.config.from_object(Config)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='yourpassword'
app.config['MYSQL_DB']='somename'


import routes