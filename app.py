from flask import Flask, request
import json
import requests
from utils import wit_response

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAMTnOQksA4BANQNFeRwIz7jJD1TZAE1UaN2F6KPEAerhyWTgpeALuCqk3eZCPoHBWWJNcYbdMcNZADZBBF3EiozqIeO490MkdaHSx1RcSc9dmzrb1nl7wZARNI8l310fud235AVN7iQ3nd6vrGfZBh0akLIQDbcaRHFAhQo0LDQZDZD'
BrandonID = '1444490405670524'
ElaineID = '1624018000992423'
CjID = '838987136226409'

@app.route('/index/')
def index():
    return "Hi I'm a chatbot"

@app.route('/', methods=['GET'])
def handle_verification():
  print "Handling Verification."
  if request.args.get('hub.verify_token', '') == 'mytoken':
    print "Verification successful!"
    return request.args.get('hub.challenge', '')
  else:
    print "Verification failed!"
    return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print "Handling Messages"
  payload = request.get_data()
  print payload
  for sender, message in messaging_events(payload):
    print "Incoming from %s: %s" % (sender, message)

    # Handle logic of responses
    response = None
    entities, values = wit_response(message)
    
    if 'permission' in entities or 'object' in entities:               # Rice cooker query       
        if 'rice cooker' in values:
            response = "Sure " + getName(PAT, sender) + ", go ahead"
            send_message(PAT, BrandonID, "I let " + getName(PAT, sender) + " use the rice cooker.")
    elif 'thanks' in entities and 'true' in values:                     # case thanks
        response = "You're welcome"
    elif 'greetings' in entities and 'true' in values:                  # case greeting
        response = "Hi " + getName(PAT, sender) + "!"
    else:
        response = "Sorry, I could not understand."
    send_message(PAT, sender, response)
  return "ok"

def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"


def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """

  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text

def getName(token, userID):
    r = requests.get("https://graph.facebook.com/v2.6/"+userID+"?",
    params={"access_token": token, "fields": "first_name"})
    if r.status_code != requests.codes.ok:
        print r.text
    return r.json()['first_name']

if __name__ == '__main__':
  app.run()