from flask import Flask,render_template, flash, redirect, request, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import mysql.connector

cur = None
try:
	print("connected")
	connection = mysql.connector.connect(user='root', password='201012', host='localhost', database='DSC') # CHANGE CREDS
	print("connected")

	cur = connection.cursor(buffered=True)
	print("connected")
except:
	print("not connected")

app = Flask(__name__,template_folder= 'templates', static_url_path = '',static_folder = 'static')
GoogleMaps(app, key="my-key")


@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'POST':
		if 'signin' in request.form:
			return redirect(url_for('signin'))
		if 'signup' in request.form:
			return redirect(url_for('signup'))
	else:
		return render_template('index.html')

@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    msg=''
    # form = SigninInputForm()
    if request.method == 'POST' and 'policeid' in request.form and 'password' in request.form:
        policeid = request.form['policeid']
        password = request.form['password']
        # if policeid == "1111" and password == "aaaa":
        #     return redirect(url_for('main'))
        cur.execute('SELECT * FROM accounts WHERE policeid = % s AND password = % s', (policeid, password))
        account = cur.fetchone()
        if account:
            session['signin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # msg = 'Signed In Successfully !'
            return redirect(url_for('main'))
        # else:
            # msg = 'Incorrect Username / Password !'
    else:
        return render_template('signin.html')



@app.route('/signup', methods = ['GET','POST'])
def signup():
    msg=''
    if request.method == 'POST' and 'fullname' in request.form and 'username' in request.form and 'policeid' in request.form and 'password' in request.form:
        fullname = request.form['fullname']
        username = request.form['username']
        policeid = request.form['policeid']
        password = request.form['password']
        cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s)', (fullname, username, policeid, password, ))
        connection.commit()
        # msg = 'You have successfully registered !'
        return redirect(url_for('main'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    else:
        return render_template('signup.html')
@app.route('/home', methods =['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        # BHALU TAKE THE VARIABLES AND ADD TO THE DATABASE
        data = request.get_json()
        crimes = data['crimes']
        print(crimes)
        return redirect(url_for('main'))
    else: 
        return render_template('form.html')

@app.route('/map', methods = ['GET', 'POST'])
def map():
    mymap = Map(

                identifier="view-side",
                varname="mymap",
                style="height:720px;width:1100px;margin:0;", # hardcoded!
                lat=37.4419, # hardcoded!
                lng=-122.1419, # hardcoded!
                zoom=15,
                markers=[(37.4419, -122.1419)] # hardcoded!

            )

    return render_template('map.html', mymap=mymap)


if __name__ == '__main__':
     app.run(debug=True)