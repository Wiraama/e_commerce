from flask import Flask
from v1.app.config import config_by_name
from v1.app.extension import app_extensions, db
from v1.app.routes.main import main

def create_app(config_name='development'):
    app = Flask(__name__)
    if config_name not in config_by_name:
        raise ValueError(f"Configuration Name {config_name} Not Found")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e_commerce.db'
    app.config.from_object(config_by_name[config_name]) # load the config name

    # initializing app fro extension
    app_extensions(app)

    # blueprints
    app.register_blueprint(main)

    return app