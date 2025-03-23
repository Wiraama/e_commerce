from v1.app.models.database import Product, db, Category
from flask import request, jsonify

# add product to database
def add_prduct():
    name = request.form.get('name')
    description = request.form.get('describtion')
    price = request.form.get('price')
    stock = request.form.get('stock')
    image_file = request.form.get('stock')
    category_id = request.form.get('category_id')

    if not all([name, category, description, price, stock, image, category_id]):
        return jsonify({"error": "All spaces must be included"}), 400
    
    # converting to appropprite types
    try:
        price = float(price)
        stock = int(stock)
    except ValueError as e:
        return jsonify({"error": f"{e}"}), 400
    
    category = Category.query.filter_by(category_id=category_id).first()

    if not category:
        return jsonify({"error": "category not found"}), 400

    # handling image file
    image = image_file.read()

    new_product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        image=image,
        category_id=category_id
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"success": "product added"}), 200