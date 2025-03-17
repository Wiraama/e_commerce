from flask import Flask
from v1.app import create_app

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=5555, debug=True)
