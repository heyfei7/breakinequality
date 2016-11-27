import os
from google.appengine.ext import db
from flask import Flask, request
from twilio.rest import TwilioRestClient
from twilio import twiml
import datetime
app = Flask(__name__)


class User(db.Model):
	phonenumber = db.StringProperty(required=True)
	duedate=db.StringProperty(required=True)

def find_week_formatted(d):
	d = str(d)
	due_day = int(d[0:2])
	due_month = int(d[3:5])
	due_year = int(d[6:])
	duedate=datetime.date(due_year,due_month,due_day)
	today = datetime.date.today()
	difference = duedate-today
	days_elapsed = 280-difference.days
	week = (days_elapsed//7)+1
	return week
@app.route("/new",methods=['GET','POST'])
def hello():
		resp = twiml.Response()
		if request.method=="POST":
			phonenumber = request.form['From']
			duedate = find_week_formatted(str(request.form['Body']))
			database = db.GqlQuery('select * from User where phonenumber = :user ', user=(phonenumber))
			flag = 0
			for data in database:
				flag = 1
			if flag==0:
				newuser=User(phonenumber = phonenumber, duedate = duedate)
				newuser.put()
			resp.message("Welcome")
			return str(resp)
		resp.message("get")
		return str(resp)
if __name__ == "__main__":
    app.run()

