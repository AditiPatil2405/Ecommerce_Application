from flask import Flask
from flask_session import Session


app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Dummy user and product data
users = {"user1": "password"}

products = {
    1: {"name": "Laptop", "price": 1000},
    2: {"name": "Mouse", "price": 50},
    3: {"name": "Keyboard", "price": 100}
}

from app import routes
