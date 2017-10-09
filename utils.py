from wit import Wit

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

# entity, value =  wit_response("Can I use the rice cooker")
# print entity
# print value

# if 'permission' in entity and 'object' in entity:
#     if 'rice cooker' in value:
#         print 'yes'