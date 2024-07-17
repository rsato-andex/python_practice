from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://docker:docker@db/python_sample'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    with app.app_context():
        from .Models.Office_Model import Office
        from .Models.System_Manager_Model import System_Manager
        from .Models.Stuff_Model import Stuff
        from .Models.User_Model import User
        db.create_all()

    login_manager.user_loader(lambda user_id: Stuff.query.get(int(user_id)))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .react import react as react_blueprint
    app.register_blueprint(react_blueprint, url_prefix='/react')

    return app
