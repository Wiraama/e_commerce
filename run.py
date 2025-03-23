from v1.app import create_app
from v1.app.extension import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=5555, debug=True)