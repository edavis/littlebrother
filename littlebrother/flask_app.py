from flask import Flask
from flask_peewee.db import Database

DATABASE = {
    'name': 'littlebrother',
    'engine': 'peewee.PostgresqlDatabase',
}

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

import context_processors
