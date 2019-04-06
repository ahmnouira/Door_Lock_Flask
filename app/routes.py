from app import App
from flask import render_template, request
from time import sleep

attempts = 0


@App.route('/index')
@App.route('/')
def index():

    return render_template("index.html")


@App.route('/unlock', methods=['POST', 'GET'])
def unlock():

    global attempts
    pwd = request.form['password'].strip()
    print(pwd)

    if attempts >= int(App.config['MAX_ATTEMPTS']):
        #sleep(10)
        return render_template('lockout.html')

    elif pwd == App.config['PASSWORD']:
        attempts = 0
        # Do someThing()exit()

        return render_template('opened.html')
    else:
        attempts += 1
        return render_template("failed.html")





