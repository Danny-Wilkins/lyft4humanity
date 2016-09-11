from flask import Flask, render_template, redirect, url_for, request
import random
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('ride_request'))
    return render_template('login.html', error=error)
@app.route('/request', methods=['GET', 'POST'])
def ride_request():
    bal = 10
    if request.method == 'POST' and bal>0: #check balance here
        return redirect(url_for('redeem_ride'))

    return render_template('request.html')
@app.route('/redeem', methods=['GET', 'POST'])
def redeem_ride():
    error = None

    randNum = "%.8d" % random.randrange(1000000,99999999)
    return render_template('success.html').format(code=randNum)
@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True, host='0.0.0.0', port = 9000)
