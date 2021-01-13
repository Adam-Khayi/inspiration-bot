import schedule
import requests
import time
import from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number
import json


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


def send_message():
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    client.messages.create(to=cellphone, from_=twilio_number, body=quote())


# send a message in the morning at 8 am EST
# schedule.every().day.at("8:00").do(send_message)

# send a message at noon
# schedule.every().day.at("12:00").do(send_message)

# send a message at night at 8 pm EST
# schedule.every().day.at("20:00").do(send_message)

# testing message
schedule.every().day.at("24:00").do(send_message())
