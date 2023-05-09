from faker import Faker
import requests
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException

from hubspot.crm.companies import SimplePublicObjectInput, ApiException

fake = Faker('en_US')

client = HubSpot(access_token="pat-na1-aeb31057-5ef2-40cb-8707-97c5bbdd73e3")



for x in range(1,1000):
    properties = {
        "city": fake.city(),
        "domain": fake.domain_name(),
        "industry": fake.bs(),
        "name": fake.company(),
        "phone": fake.phone_number(),
        "country": fake.country()

    }

    simple_public_object_input_for_create = SimplePublicObjectInput(properties=properties) 
        
    try:
        api_response = client.crm.companies.basic_api.create(simple_public_object_input=simple_public_object_input_for_create , async_req=True)
        print(api_response.get())
    except ApiException as e:
        print("Exception when calling basic_api->create: %s\n" % e)