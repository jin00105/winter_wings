from flask import Flask
#from flask import Flask, render_template, url_for
#from flask import request, redirect, jsonify, flash
#import random
#import string
#import httplib2
#from flask import make_response
#import requests

app = Flask(__name__)

# main page
#@app.route('/')
#@app.route('/winterwings')
#def main():
#	return  'Hello World!' #render_template('main.html')

@app.route('/')
@app.route('/hello')
def HelloWorld():
	return "Hello World"

if __name__ == '__main__':
#	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)