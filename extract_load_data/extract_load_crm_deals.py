from hubspot import HubSpot
import json
import pymongo
from pymongo.mongo_client import MongoClient
import pandas as pd
import datetime
from pymongo.server_api import ServerApi
from hubspot.crm.companies import ApiException
import requests

access_token = 'pat-na1-aeb31057-5ef2-40cb-8707-97c5bbdd73e3'
api_client = HubSpot(access_token=access_token)

db_client = MongoClient(
    "mongodb+srv://viraj:viraj@etl.cy6ldzf.mongodb.net/?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)
db = db_client.Test

collection = db.HubSpot_CRM_Companies_tester_for_throttling

headers = {'Authorization' : f'Bearer {access_token}'}
url = 'https://api.hubapi.com/crm/v3/objects/deals'
data = []
try:
    keep_going = True
    while keep_going:        
        api_response = requests.get( url  , headers=headers)
     
        if 'paging' in api_response.json().keys():
            data = data + api_response.json()['results']
            url = api_response.json()['paging']['next']['link']
            # print(data)
        else:
            data = data + api_response.json()['results']
            # print(data)
            keep_going = False
        
        
     
    print(len(data))
except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)

 
collection.insert_many(data)








