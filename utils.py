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


# entities, values = wit_response("Hi")
# print entities
# print values