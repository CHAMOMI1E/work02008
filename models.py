from main import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/test"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SMTH(db.Model):
    __tablename__ = 'test'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    js = db.Column(db.JSONB)

    def __init__(self, name, js):
        self.name = name
        self.js = js

    def __repr__(self):
        return f"<Car {self.name}>"
