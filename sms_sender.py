from twilio.rest import Client
import sys


account_sid = 'ACc7a1c4db76fb0486f35e6f31a3e06a1e'
auth_token = 'f088cd5d241aebb6606b63b4b7140e85'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+13342922550',
    body='This is Jordin. I\'m sending this from a program I built for school, not a phone. Crazy right!?',
    to='+12543945535'
)

print(message.sid)
