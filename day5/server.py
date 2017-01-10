from flask import Flask, render_template
import os

# Set up Flask server
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder = template_folder)

# Set up functions for Flask to handle requests
@app.route('/', methods = ['GET'])
def index():
	return 'Hello world'

@app.route('/hello', methods = ['GET'])
def hello():
	return render_template('hello.html')

@app.route('/fancy', methods = ['GET'])
def fancy():
	return render_template('fancy.html')

# Run Flask server
app.run(host = '0.0.0.0', port = 8080, debug = True, threaded = False)