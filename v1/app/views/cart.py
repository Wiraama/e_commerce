from v1.app.models.database import Cart, Product, db
from flask import request, jsonify

def create_cart():
    product_id = request.form.get('product_id')
    user_id = request.form.get('user_id')
    quantity = request.form.get('quantity')

    if not all([product_id, user_id, quantity]):
        return jsonify({"error": "Some details are missing"}), 400

    product = Product.query.filter_by(id=product_id).first()
    new_item = Cart(
        user_id=user_id,
        product_id=product_id,
        product_name=product.name,
        image = product.image,
        product_price = product.price,
        quantity = quantity
    )

    db.session.add(new_item)
    db.session.commit()

    return jsonify({"success", "item added to cart"})

def request_cart():
    #initializing
    cart = Cart.query.all()
    price_count = 0
    count = 0

    # finding totals in cart
    count = len(cart)
    price_count = sum(item.product_price for item in cart if item.product_price)

    totals = {
        "total_items": count,
        "total_price": price_count
    }

    return totals, cart