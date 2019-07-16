from flask import Flask 		# import Flask 
from flask_bootstrap import Bootstrap	# import Bootstrap
from app.config import Config                       # import Config class
App = Flask(__name__)		# create Flask object
boostrap = Bootstrap(App)                             # create Bootstrap object
App.config.from_object(Config)                     # sets the configuration from Config                      
from app import routes 		# import routes
