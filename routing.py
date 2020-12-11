from flask import Flask,render_template, flash, redirect, request, url_for

import mysql.connector

cur = None
try:
	print("connected")
	connection = mysql.connector.connect(user='root', password='test', host='localhost', database='DBMS') # CHANGE CREDS
	print("connected")

	cur = connection.cursor(buffered=True)
	print("connected")
except:
	print("not connected")

app = Flask(__name__,template_folder= 'templates', static_url_path = '',static_folder = 'static')

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
	return render_template('signin.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():
	return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)

