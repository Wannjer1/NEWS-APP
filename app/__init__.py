from flask import Flask 
from flask_bootstrap import Bootstrap
from pip import main
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):


    # initializing application
    app = Flask(__name__,instance_relative_config=True,static_url_path='/static')

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing Flask extension
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app
