from flask import Flask, render_template

main = Flask(__name__)

@main.route("/")
def index():
    render_template('index.html')