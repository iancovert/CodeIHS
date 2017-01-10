from flask import Flask, render_template, request
import os
from bank import Bank

'''
	First, we handle everything related to the bank. That means creating a bank
	object, creating accounts, and putting money in them
'''

# TODO

'''
	Next, we handle everything related to our server. THat means instructing it
	where to find files (the templates folder), and instructing it how to
	respond to a number of different requests
'''

# Set up Flask server
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder = template_folder)

# Routes for responding to HTTP requests
@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html', bank = bank)


@app.route('/deposit', methods = ['GET'])
def deposit():
	return render_template('deposit.html', bank = bank)


@app.route('/withdraw', methods = ['GET'])
def withdraw():
	return render_template('withdraw.html', bank = bank)


@app.route('/accounts', methods = ['GET'])
def accounts():
	return render_template('accounts.html', bank = bank)

@app.route('/depositAttempt', methods = ['POST'])
def depositAttempt():
	name = request.form['name']
	amount = float(request.form['amount'])
	pin = int(request.form['pin'])

	# TODO

	return render_template('transaction_complete.html', result = result)
	
@app.route('/withdrawAttempt', methods = ['POST'])
def withdrawAttempt():
	name = request.form['name']
	amount = float(request.form['amount'])
	pin = int(request.form['pin'])

	# TODO
	
	return render_template('transaction_complete.html', result = result)

'''
	Finally, we start our server
'''

# Start server
app.run(host = '0.0.0.0', port = 8080, debug = True, threaded = False)