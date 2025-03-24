from flask import  Blueprint, render_template
from v1.app.views.cart import request_cart
from v1.app.views.products import add_product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    totals, cart = request_cart()
    return render_template('index.html', cart=cart, totals=totals)

@main.route('/admin', methods=['GET', 'POST'])
def admin():
    products = add_product()
    return render_template('admin.html', products=products)