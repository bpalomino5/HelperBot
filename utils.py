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

# response = "Sorry, I could not understand \U0001f61e"  # base case
# entities, values = wit_response("rice cooker?")
# print "entities: %s " % entities        #DEBUG
# print "values: %s " % values            #DEBUG

# if 'permission' in entities or 'object' in entities:               # Rice cooker query       
#     if 'rice cooker' in values:
#         response = "Sure " + getName(PAT, sender) + ", go ahead"
#         send_message(PAT, BrandonID, "I let " + getName(PAT, sender) + " use the rice cooker.")
# if 'thanks' in entities and 'true' in values:                     # case thanks
#     response = "You're welcome"
# if 'greetings' in entities and 'true' in values:                  # case greeting
#     response = "Hi " + getName(PAT, sender) + "!"
# print response