import os
from flask import Flask
from dotenv import load_dotenv
from peewee import PostgresqlDatabase

load_dotenv()
app = Flask(__name__)
DB_NAME = os.environ.get("POSTGRES_DB")
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = 5432  # os.environ.get("POSTGRES_PORT")

db = PostgresqlDatabase(
    DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)

@app.route("/")
def start():
    pass


if __name__ == '__main__':
    app.run()
