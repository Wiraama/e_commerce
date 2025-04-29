from v1.app.models.database import Product, db
from flask import request, jsonify, redirect, url_for
import os, uuid
from  werkzeug.utils import secure_filename

def store_file(file):
    print("am on store file")
    folder = "v1/app/static/uploads"
    os.makedirs(folder, exist_ok=True)
    
    _, ext = os.path.splitext(secure_filename(file.filename))
    filename = f"{uuid.uuid4()}{ext}"
    
    storage_path = os.path.join(folder, filename)
    file.save(storage_path)
    
    sliced_path = storage_path[6:]
    print(sliced_path)
    print("image done")
    return sliced_path
    
# add product to database
def add_product():
    print("am on product")
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    x_price = request.form.get('x-price')
    stock = request.form.get('stock')
    image_file = request.files.get('image')
    category_name = request.form.get('category')

    if not all([name, x_price, category_name, description, price, stock, image_file]):
        print("am in if not")
        return jsonify({"error": "All spaces must be included"}), 400
    print("done takiing from html")
    # converting to appropprite types
    try:
        price = float(price)
        stock = int(stock)
    except ValueError as e:
        return jsonify({"error": f"{e}"}), 400

    # handling image file
    image_url = store_file(image_file)
    print("done image url take")
    new_product = Product(
        name=name,
        description=description,
        price=price,
        x_price=x_price,
        stock=stock,
        image=image_url,
        category_name=category_name
    )

    db.session.add(new_product)
    db.session.commit()

    print("added")
    return redirect(url_for('main.admin'))

def delete_product(product_id):
    if not (product_id):
        print("no product id")
        return jsonify({"error": "Missing product_id"}), 400
    
    product = Product.query.filter_by(id=product_id).first()
    
    if not(product):
        print("no Product")
        return jsonify({"error": "Product not Found"}), 400
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"success": "Product deleted successfully", "product_id": product_id})
    
