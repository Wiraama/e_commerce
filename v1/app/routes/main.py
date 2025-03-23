from flask import  Blueprint, render_template
from v1.app.views.cart import request_cart

main = Blueprint('main', __name__)

@main.route('/')
def index():
    cart, totals = request_cart()
    return render_template('index.html', cart=cart, totals=totals)