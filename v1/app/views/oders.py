from flask import request
from v1.app.models.database import Order, Product, User

def add_order():
    email = request.form.get(email=email)
    product_id = request.form.get('product_id')
    user = User.query.filter_by(email=email).first()