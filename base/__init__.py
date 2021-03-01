from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'shdbfhrudcjajv'

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/clothesshopingusingar'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

database = SQLAlchemy(app)

import base.com.controller
