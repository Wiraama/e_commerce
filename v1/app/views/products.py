from v1.app.models.database import Product, db, Category
from flask import request, jsonify

# add product to database
def add_product():
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    stock = request.form.get('stock')
    image_file = request.files.get('image')
    category_name = request.form.get('category')

    if not all([name, category_name, description, price, stock, image_file]):
        return jsonify({"error": "All spaces must be included"}), 400
    
    # converting to appropprite types
    try:
        price = float(price)
        stock = int(stock)
    except ValueError as e:
        return jsonify({"error": f"{e}"}), 400
    
    category = Category.query.filter_by(category=category_name).first()

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
        category_id=category.id
    )

    db.session.add(new_product)
    db.session.commit()

    products = Product.query.all()

    return products