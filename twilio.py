from twilio.rest import Client
import json


with open('data/config.json') as json_file:
  config = json.load(json_file)

account_sid = config.get('twilio_accountSID')
auth_token = config.get('twilio_token')
number = config.get('twilio_phoneNumber')

client = Client(account_sid, auth_token)


message = client.messages.create(
         body='Coucou my love',
         from_=number,
         to=''
         )

print(message.sid)
