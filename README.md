# TwilioFireText
Simple web app to send text messages to any phone number.

### How to Run the Web App

We are using Twilio API to send text messages.

#### Prerequisites

- python
- pip
- flask
- twilio
- configobj

### Setup

1. Create account on Twilio (https://www.twilio.com/) and get your Twilio SID, Twilio Token, and Twilio phone number.
 * Twilio SID, Twilio Token can be found on the "Console Dashboard" when you login into Twilio.
 * Twilio phone number can be obtained at https://www.twilio.com/console/phone-numbers/incoming , this is not your phone number. 

2. . Download and save all the files from "myWebApp" folder on your local computer.

3.  Go to the terminal, then go to the folder where you saved all the file (for example "myWebApp") run command `python flaskFile.py` on your terminal while you are inside the base folder (folder containing flaskFile.py).

4.  Open the web browser and enter `http://127.0.0.1:5000/message` in the address bar and 
### voila !!! You are ready to send text messages
