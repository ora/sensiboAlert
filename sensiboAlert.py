#!/usr/bin/env python3

# https://github.com/ora/sensiboAlert
# This will check Sensibo API & alert via email (SendGrid) if Sensibo is offline or temperature falls

import requests
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

sensibo_apiKey = "SENSIBO APIKEY"
sg_apiKey = "SENDGRID APIKEY"
sendTo = "EMAIL ADDRESS"

resp = requests.get("https://home.sensibo.com/api/v2/users/me/pods?fields=connectionStatus{isAlive},measurements&apiKey=%s" %(sensibo_apiKey))

if not resp:
    print("%s: Exiting" %resp.status_code)
    exit()

data = resp.json()

temperature = (int(round((9 * data["result"][0]["measurements"]["temperature"]) / 5 + 32)))

print("Response:", resp.status_code)
print("Status:", data["result"][0]["connectionStatus"]["isAlive"])
print("Temperature:", temperature)

def sendMail(alert_body):
	message = Mail(from_email='sensibo_alert@no_reply.com', to_emails=sendTo, subject='Sensibo Alert', html_content=alert_body)
	sg = SendGridAPIClient(sg_apiKey)
	response = sg.send(message)
	print(response.status_code)
	print(response.body)
	print(response.headers)

if ((data["result"][0]["connectionStatus"]["isAlive"]) == 0):
	sendMail("<strong>Sensibo is offline<strong>")

if (temperature < 56):
	sendMail("<strong>Sensibo temperature is " + str(temperature) + "<strong>")
