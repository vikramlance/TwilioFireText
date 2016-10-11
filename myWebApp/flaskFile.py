'''
Web app components
front end, back end, database 

We are using Twilio API to send text messages.

install 
python
pip
flask
twilio
configobj
Create account on TWILIO and get your Twilio SID, Twilio Token, and Twilio Phone number

'''

import requests
from requests.auth import HTTPBasicAuth
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request
from configobj import ConfigObj

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')

def home(name=''):
	return render_template('home.html',name='Vikram')
	
@app.route('/message', methods=['GET','POST'])
def message():
	if request.method == 'GET':
		return render_template('message.html')
	else:
		number = request.form['phoneNumber']
		message = request.form['message']
		client = TwilioRestClient('TWILIO_SID', 'TWILIO_TOKEN') #(TWILIO_SID, TWILIO_TOKEN)
		# both the parameters can be obtained on "Console Dashboard" when you login into TWILIO
		message = client.messages.create(body=message,
			to="+1"+number,
			from_='TWILIO_PHONE_NUMBER') # replace with your twilio number (it's not your phone number), 
			#TWILIO phoneNumber can be obtain at https://www.twilio.com/console/phone-numbers/incoming
      #Put phone number withhout country code as we already added +1
		return render_template('message.html',
			success="You sent a bloody message")
if __name__=='__main__':
	app.run()
