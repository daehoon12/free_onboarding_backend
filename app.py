import sqlite3

from flask import Flask
from flask_restx import Api
from crud import Todo
from auth import Auth
import database

app = Flask(__name__)
app.secret_key='wecode'
api = Api(app)

db = database.connect_db()
db.execute('''CREATE TABLE members
                 (id char, password char)''')
db.execute('''CREATE TABLE post_info
                 (id char, post_no int, data text, created_date text, modified_date text)''')


api.add_namespace(Todo, '/posts')
api.add_namespace(Auth, '/auth')

if __name__ == "__main__":
    app.run()