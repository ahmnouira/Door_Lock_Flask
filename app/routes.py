from app import App			# import App object from __init__.py
from flask import render_template                 # import render_template to render the .html file

@App.route('/index')			# decorator 
@App.route('/')
def index():			# view function 
    return render_template("index.html")         # the response







