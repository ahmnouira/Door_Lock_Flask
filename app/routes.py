from app import App			        # import App object from __init__.py
from flask import render_template                         # import render_template to render the .html file
from flask import request                                       # import request to get password input

attempts = 0                                                            # variable stores attempts 

@App.route('/index')			         # decorator : sets the URL for view function
@App.route('/')                                                
def index():			          # view function 
    return render_template("index.html")                   # the response


@App.route('/unlock', methods=['POST', 'GET'])        # decorator for '/unlock' 
def unlock():                                                               # view function 
    global attempts                                                      # attempts global variable
    pwd = request.form['password'].strip()                  # read password from the form without spaces chars
    print(pwd)

    if attempts >= App.config['MAX_ATTEMPTS']:       # To many attempts
        return render_template('lockout.html')

    elif pwd == App.config['PASSWORD']:                     # success 
        attempts = 0
        # Do someThing()
        return render_template('opened.html')
                                                                                 
    else:                                                                         # failed
        attempts += 1
        return render_template("failed.html")





