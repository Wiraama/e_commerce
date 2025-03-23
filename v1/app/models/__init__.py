# initializing folder
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .database import User, Order, OrderItem, Product, Payment