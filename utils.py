from wit import Wit
import requests

access_token = "EO6GJLEDDW7SJ3L6BJSMALGU5JA2UAQI"

client = Wit(access_token = access_token)

def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entities = list(resp['entities'])
        values = []
        for entity in entities:
            values.append(resp['entities'][entity][0]['value'])
    except:
        pass
    return(entities, values)

"""
response = "Sorry, I could not understand"  # base case
entities, values = wit_response("notify elaine that i love you!")
print "entities: %s " % entities        #DEBUG
print "values: %s " % values            #DEBUG

if 'permission' in entities or 'object' in entities:               # Rice cooker query       
    if 'rice cooker' in values:
        response = "Sure " + getName(PAT, sender) + ", go ahead"
        send_message(PAT, BrandonID, "I let " + getName(PAT, sender) + " use the rice cooker.")
if 'thanks' in entities and 'true' in values:                     # case thanks
    response = "You're welcome"
if 'greetings' in entities and 'true' in values:                  # case greeting
    response = "Hi " + getName(PAT, sender) + "!"
if 'command' in entities and 'user' in entities and 'message_body' in entities: # case command tell with user
    command = values[entities.index('command')]
    message = values[entities.index('message_body')]   # gathering message_body with minimal error
    user = values[entities.index('user')]   # getting user value
    senderID = None
    if user == 'Elaine':
        senderID = "ElaineID"
    elif user == 'Bryan':
        senderID = "BryanID"
    elif user == 'CJ':
        senderID = "CjID"
    else:
        print 'this error needs be handled!'

    if command == 'notify':
        response = "Elaine, " + message
    else:
        response = "Elaine, " + "Brandon says " + message
print response
"""