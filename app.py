from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "https://your-app.vercel.app"])
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

from models import db
db.init_app(app)

with app.app_context():
    db.create_all()

from routes import *

if __name__ == "__main__":
    app.run(debug=True)
