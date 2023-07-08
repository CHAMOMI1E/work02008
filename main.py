from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import JSONB
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test_username:test_password@localhost:54321/test_db"
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


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        data = request.form.getlist('name[]')
        some_json=json.dumps(dict(zip([str(i) for i in range(1,len(data)+1)], data)))
        print(some_json)
        db.session.add(TestModel(json_column=some_json))
        db.session.commit()
        return redirect('/read')
    else:
        return render_template('create.html')
