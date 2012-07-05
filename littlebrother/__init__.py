from flask import Flask
from flask_peewee.db import Database

DATABASE = {
    'name': 'littlebrother',
    'engine': 'peewee.PostgresqlDatabase',
}

DEBUG = True
RESULTS_PER_PAGE = 50

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

import web
import context_processors
