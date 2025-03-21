from v1.app.models.database import db, User
from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from flask_bcrypt import Bcrypt
from v1.app.views.user import user_register

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

#register user to database
@auth.route('register', methods=['GET', 'POST'])
def add_user():
    return user_register()

# login part
@auth.route("/auth", methods=['POST', 'GET'])
def login():
    # requesting data from frontend
    email = request.form.get('email')
    password = request.form.get('password')

    # checking if user exist and verifiying
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "Email not Registered"}), 400

    if bcrypt.check_password_hash(user.hash_password, password):
        return redirect(url_for('home'))
    else:
        return jsonify({"error": "password mismatch\ntry again"})