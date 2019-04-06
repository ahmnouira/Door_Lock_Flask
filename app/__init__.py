from flask import Flask 
from flask_bootstrap import Bootstrap
from app.config import Config
App = Flask(__name__)
bootstrap = Bootstrap(App)
App.config.from_object(Config)
from app import routes
