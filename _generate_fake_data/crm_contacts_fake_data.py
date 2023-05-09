from faker import Faker
import requests
from hubspot import HubSpot

from hubspot.crm.contacts.exceptions import ApiException

from hubspot.crm.contacts import SimplePublicObjectInput, ApiException

fake = Faker('en_US')

access_token = 'pat-na1-aeb31057-5ef2-40cb-8707-97c5bbdd73e3'

client = HubSpot(access_token= access_token)


for x in range(1,1000) :
    url = 'https://api.hubapi.com/crm/v3/objects/contacts'
    
    properties = {
        "company": fake.company(),
        "email": fake.email(),
        "firstname": fake.name(),
        "lastname": fake.name(),
        "phone": fake.phone_number(),
        "website": fake.domain_name()
    }
    simple_public_object_input_for_create = SimplePublicObjectInput(properties=properties)
    
    try:
        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=simple_public_object_input_for_create , async_req=True)
        print(api_response.get())
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)
    
