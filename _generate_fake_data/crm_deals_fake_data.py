from faker import Faker
import random
import hubspot
from pprint import pprint
from hubspot.crm.deals import SimplePublicObjectWithAssociations, ApiException

client = hubspot.Client.create(access_token="pat-na1-aeb31057-5ef2-40cb-8707-97c5bbdd73e3")

fake = Faker('en_US')

access_token = 'pat-na1-aeb31057-5ef2-40cb-8707-97c5bbdd73e3'

for x in range(0,1000):

    properties = {
            "amount": f'{random.randint(10,10000)}',
            "closedate": f'{fake.date()}',
            "dealname": f'{fake.pystr()}',
            "dealstage": random.choice(["presentationscheduled" , "closedwon" , "appointmentscheduled" , 'qualifiedtobuy' , 'decisionmakerboughtin' , 'contractsent' , 'closedlost']),
            "pipeline": "default"
        }
    simple_public_object_input_for_create = SimplePublicObjectWithAssociations(properties=properties, associations=[{"to":{"id":"1"},"types":[{"associationCategory":"HUBSPOT_DEFINED","associationTypeId":3}]}])
    try:
        api_response = client.crm.deals.basic_api.create(simple_public_object_input=simple_public_object_input_for_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)





