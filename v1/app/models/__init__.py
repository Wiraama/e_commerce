# initializing folder
from flask import SQLAlchemy

db = SQLAlchemy()

from .database import User, Oder, OrderItem, Product, Payment