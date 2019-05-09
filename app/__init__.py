from flask import Flask 		#import Flask 
from flask_bootstrap import Bootstrap	#import Bootstrap
App = Flask(__name__)		#create Flask object
boostrap = Bootstrap(App)                             #create bootstrap object
from app import routes 		#import routes
