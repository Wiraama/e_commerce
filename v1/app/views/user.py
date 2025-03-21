from v1.app.models.database import db, User
from flask import request, render_template, jsonify
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# registering user
def user_register():
    # requesting info from fronted
    email = request.form.get('email')
    f_name = request.form.get('f_name')
    l_name = request.form.get('l_name')
    hash_password = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
    role = request.form.get('role')
    created_at = datetime.now()

    name = " ".join([f_name, l_name])

    if not all([email, name, hash_password, role, created_at]):
        return jsonify({"error": "All fields are required"}), 400

    user = User.query.filter_by(email=email).first()

    # checking if email exist in database
    if user:
        return jsonify({"error": "Email exist"}), 400
    
    # add new user
    new_user = User(
        email=email,
        hash_password=hash_password,
        created_at=created_at,
        name=name,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()
    return render_template('register.html')