from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.create_users_table()
db.create_todos_table()