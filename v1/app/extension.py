from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

"""initializing """
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()

def app_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    """ user loader """
    if not login_manager._user_callback:
        @login_manager.user_Loader
        def load_user(user_id):
            return User.query.get(int(user_id))