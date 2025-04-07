from v1.app.models.database import Product, db
from flask import request, jsonify 
import os, uuid
from  werkzeug.utils import secure_filename

def store_file(file):
    folder = "v1/app/static/uploads"
    os.makedirs(folder, exist_ok=True)
    
    _, ext = os.path.splitext(secure_filename(file.filename))
    filename = f"{uuid.uuid4()}{ext}"
    
    storage_path = os.path.join(folder, filename)
    file.save(storage_path)
    
    sliced_path = storage_path[6:]
    print(sliced_path)
    return sliced_path
    
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

    # handling image file
    image_url = store_file(image_file)

    new_product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock,
        image=image_url,
        category_name=category_name
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"sucess" : "Product added"})