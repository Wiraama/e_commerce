from flask import  Blueprint, render_template, request, redirect, url_for
from v1.app.views.cart import request_cart
from v1.app.views.products import add_product
from v1.app.models.database import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    totals, cart = request_cart()
    return render_template('index.html', cart=cart, totals=totals)

@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        add_product()
        return redirect(url_for('main.admin'))
    products = Product.query.all()
    list(map(lambda product: print(product.image), products))
    return render_template('admin.html', products=products)