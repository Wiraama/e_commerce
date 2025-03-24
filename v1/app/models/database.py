from flask_login import UserMixin # to manage session correctly
from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from sqlalchemy.types import Enum as SQLAlchemyEnum
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()

"""
    User - for customers
    Product - for product details
    Category - categorize product
    Oder - customer orders
    Order item - items in order
    Payment - tracks Payments
    Review - reviews made
"""
class User(db.Model, UserMixin):
    """User data"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(15), default="customer")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    order = db.relationship("Order", backref="customer", lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"
    
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Category {self.category}>"

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(10), nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)

    def __repr__(self):
        return f"<Product {self.name} - Category: {self.category.id}>"

  

class Cart(db.Model):
    # cart class
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(55), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.String(20), default="pending") # shipping, delivered, ready for pickup
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    products = db.Column(db.String(255), nullable=False) # maximum 10 items

    order_items = db.relationship("OrderItem", backref="order", lazy=True)

    def __repr__(self):
        return f"<Order {self.id} - Status {self.status}>"
    
class OrderItem(db.Model):
    __tablename__ = "orderitem"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    product = db.relationship("Product", backref="order_items")

    def __repr__(self):
        return f"<OrderItem: {self.order_id} Product: {self.product_id}>"

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(20), nullable=False, default="waiting")
    transaction_id = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", backref="payment")

    def __repr__(self):
        return f"<Payment {self.transaction_id} Amount: {self.amount} Status: {self.payment_status}>"
    
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    rating = db.Column(db.Integer, nullable=False) # rating 1-5
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    user = db.relationship("User", backref="reviews")
    product = db.relationship("Product", backref="reviews")

    def __repr__(self):
        return f"<Reviews {self.product_id} Rating {self.rating}>"