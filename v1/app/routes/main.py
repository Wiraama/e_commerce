from flask import  Blueprint, render_template, request, redirect, url_for
from v1.app.views.cart import request_cart
from v1.app.views.products import add_product, delete_product
from v1.app.models.database import Product

main = Blueprint('main', __name__)

@main.route('/')
def index():
    totals, cart = request_cart()
    products = Product.query.order_by(Product.id.desc()).all()
    list(map(lambda product: print(product.image), products))

    return render_template('index.html', cart=cart, totals=totals, products=products)

@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return redirect(url_for('main.admin'))

    products = Product.query.order_by(Product.id.desc()).all()
    list(map(lambda product: print(product.image), products))
    return render_template('Admin.html', products=products)

@main.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    product_id = data.get('product_id')
    return(delete_product(product_id))

@main.route('/main.not-created')
def not_created():
    return render_template('not-created.html')
