from flask import Flask,render_template, flash, redirect, request, url_for, session
import requests
import sys
sys.path.append('..')
import ML_Classifier.predict
from ML_Classifier.predict import predict2
import ML_Classifier.scoring
from ML_Classifier.scoring import total_score, minor_crimes_score, major_crimes_score, vehicle_infractions_score, sex_offenses_score, other_crimes_score
# import mysql.connector
import sqlite3
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
#import predict
from math import sin, cos, sqrt, atan2
from datetime import datetime
from calendar import month_abbr
import random

# cur = None
# try:
print("ready1")
cur = sqlite3.connect('dsc.db', check_same_thread=False)
# connection = mysql.connector.connect(user='root', password='your_password', host='localhost', database='dsc', auth_plugin='mysql_native_password') # CHANGE CREDS
print("ready2")

# cur = connection.cursor(buffered=True)
# print("ready3")
# except:
# 	print("not connected")

app = Flask(__name__,template_folder= 'templates', static_url_path = '',static_folder = 'static')
GoogleMaps(app, key="my-key")
source = requests.get('https://www.indiatoday.in/crime')
content = source.content
soup1 = BeautifulSoup(content, 'html5lib')
news_art = soup1.find_all('div',class_ = 'catagory-listing')

def dist(lat, lon, radius):
    map_list = []
    cur.execute('SELECT * FROM fir')
    dist_list = cur.fetchall()
    for item in dist_list:
        lon2 = item['longitude']
        lat2 = item['latitude']
        dlon = lon2 - lon
        dlat = lat2 - lat
        a = (sin(dlat/2))**2 + cos(lat) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        if distance <= radius:
            map_list.append(item)
    return map_list


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
    if request.method == 'POST':
        print('hi')
        if 'policeid' in request.form and 'password' in request.form:
            policeid = request.form['policeid']
            password = request.form['password']
            print('hi')
        # if policeid == "1111" and password == "aaaa":
        #     return redirect(url_for('main'))
            # cur.execute('SELECT * FROM accounts WHERE policeid = % s AND password = % s', (policeid, password))
            # account = cur.fetchone()
            # if account:
            #     session['signin'] = True
            #     session['id'] = account['id']
            #     session['username'] = account['username']
            # msg = 'Signed In Successfully !'
            return redirect(url_for('main'))
        # else:
            # msg = 'Incorrect Username / Password !'
    else:
        return render_template('signin.html')



@app.route('/signup', methods = ['GET','POST'])
def signup():
    msg=''
    if request.method == 'POST':
        if 'fullname' in request.form and 'username' in request.form and 'policeid' in request.form and 'password' in request.form:
            fullname = request.form['fullname']
            username = request.form['username']
            policeid = request.form['policeid']
            password = request.form['password']
            #cur.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s)', (fullname, username, policeid, password, ))
            #connection.commit()
        # msg = 'You have successfully registered !'
            return redirect(url_for('main'))
        else:
            msg = 'Please fill out the form !'
    else:
        return render_template('signup.html')
@app.route('/main', methods =['GET', 'POST'])
def main():
   #print(news_art)
    images =[]
    titles = []
    descs = []
    for i in news_art:
        image = i.find('img')['src']
        images.append(image)
        title = i.find('h2').get_text()
        titles.append(title)
        desc = i.find('p').get_text()
        descs.append(desc)

    month = datetime.now().month   # current month number
    month_list = [month_abbr[(month % 12 + i) or month] for i in range(12)]

    x = month_list
    y = [i+random.randint(0,100) for i in range(0,12)]
    plt.plot(x,y)
    plt.gcf().autofmt_xdate()

    #plt.show()
    plt.savefig('./static/images/plot.png' , bbox_inches='tight')
    print('smit')

    return render_template('main2.html',images = images, titles = titles, descs = descs, url ='./static/images/plot.png')


@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = request.get_json()
        details = data['object']
        fullname = details['fullname']
        firnumber = details['firnumber']
        phonenumber = details['phonenumber']
        empdetails = details['empdetails']
        interviewscore = details['interviewscore']
        latitude = details['latitude']
        longitude = details['longitude']
        scoreraw = 0
        scoremajorcrimes = 0
        scoreminorcrimes = 0
        scorevehicleinfractions = 0
        scoresexoffenses = 0
        scoreothers = 0
        criminalnature = "citizen"
        filestatus = "pending"
        policeresponse = "pending"
        crime = details['crime']
        print('CRIME' + crime)
        predoutput = predict2(crime)
        crimes = data['crimes']
        print(crimes)
        print(fullname)
        print(type(predoutput))
        # predoutput = predict2(crimes)
        # # print(crimes)
        for c in predoutput:
            scoreraw += total_score(predoutput[c])
            scoremajorcrimes += major_crimes_score(predoutput[c])
            scoreminorcrimes += minor_crimes_score(predoutput[c])
            scorevehicleinfractions += vehicle_infractions_score(predoutput[c])
            scoresexoffenses += sex_offenses_score(predoutput[c])
            scoreothers += other_crimes_score(predoutput[c])
        cur.execute("INSERT INTO fir(fullname, firnumber, phonenumber, empdetails, interviewscore, latitude, longitude, scoreraw, \
            scoremajorcrimes, scoreminorcrimes, scorevehicleinfractions, scoresexoffenses, scoreothers, criminalnature, filestatus, \
                policeresponse) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",(fullname, firnumber, phonenumber, empdetails, \
                    interviewscore, latitude, longitude, scoreraw, scoremajorcrimes, scoreminorcrimes, scorevehicleinfractions, \
                        scoresexoffenses, scoreothers, criminalnature, filestatus, policeresponse))
        cur.commit()
        
        return redirect(url_for('main'))
    else: 
        return render_template('form.html')


@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        option = request.form['crime_category']
        if option == "majc":
            cur.execute("SELECT fullname, scoremajorcrimes FROM fir ORDER BY scoremajorcrimes DESC;")
            cur.commit()
        elif option == "minc":
            cur.execute("SELECT fullname, scoreminorcrimes FROM fir ORDER BY scoreminorcrimes DESC;")
            cur.commit()
        elif option == "sex":
            cur.execute("SELECT fullname, scoresexoffenses FROM fir ORDER BY scoresexoffenses DESC;")
            cur.commit()
        elif option == "veh":
            cur.execute("SELECT fullname, scorevehicleinfractions FROM fir ORDER BY scorevehicleinfractions DESC;")
            cur.commit()
        elif option == "oth":
            cur.execute("SELECT fullname, scoreothers FROM fir ORDER BY scoreothers DESC;")
            cur.commit()
    else:
        return render_template('mostwtd.html')


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
