from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
# from flask_moment import Moment - used for JS date and time conversions




db = SQLAlchemy()

migrate = Migrate()
# create LoginManager object and configure the login view as 'auth.login', i.e, `login` route in `auth` Blueprint. 
login = LoginManager()
login.login_view = 'auth.login'
# create Moment object
#moment = Moment()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER_MAIN

    csrf = CSRFProtect(app)

    db.init_app(app)
    migrate.init_app(app,db)
    # Configure the app object for login using `init_app` function. 
    login.init_app(app)
    # Configure the app object for moment using `init_app` function. 
    #moment.init_app(app)

    # blueprint registration
    from app.main.home import main_blueprint as main
    main.template_folder = Config.TEMPLATE_FOLDER_MAIN
    app.register_blueprint(main)

    from app.auth import auth_blueprint as auth
    auth.template_folder = Config.TEMPLATE_FOLDER_AUTH
    app.register_blueprint(auth)

    from app.main.lasker_morris import laskermorris_blueprint as lm
    lm.template_folder = Config.TEMPLATE_FOLDER_LM
    app.register_blueprint(lm)

    from app.errors import error_blueprint as errors
    errors.template_folder = Config.TEMPLATE_FOLDER_ERRORS
    app.register_blueprint(errors)

    return app
