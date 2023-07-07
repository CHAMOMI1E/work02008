import flask

from models import *
from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSONB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:02082002@localhost:5433/test_db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TestModel(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    json_column = db.Column(JSONB)

    def __init__(self, json_column):
        self.json_column = json_column

    def __repr__(self):
        return f"<Car {self.name}>"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/read')
def read():
    smth = TestModel.query.all()
    return render_template('read.html', smth=smth)


@app.route('/create')
def create():
    if request.method == "post":
        text = request.form['name']
        print(text)
        return url_for('home')
    else:
        return render_template('create.html')
