import requests
import json
from utilities.DriverWrapper import DriverWrapper
from utilities.settings import *

class MyRequests:

    request_data_time = {
        "filial_id": 2382,
        "tiket_token": ticket_token
    }

    def get_free_time(self):
        response = requests.get(request_url, self.request_data_time)
        print(response)
        return response

    def get_lagers(self):

        get_lager_request = {
            'filial_id': 2382,
            'user_id': "56"
        }

        my_response = requests.get(get_lagers_url, get_lager_request)
        print(my_response)
        lager_dict = my_response.json()
        for lager in lager_dict['lagers']:
            print(lager, '\n')
            if lager['remnant'] > 0:
                print(lager['remnant'])

            # remnant = (lager['lagers'][0]['remnant'])
            # print(lager)



        # test = my_response.json()

        # print(test['lagers'][0]['remnant'])

    def create_lagers_in_basket(self):
        headers = {
            "accept": "text/plain",
        "Content-Type": "application/json-patch+json"
        }

        lager = {
            "ticketToken": "string",
            "filialId": 0,
            "lager": {
                "id": 0,
                "count": 0
            }
        }

        requests_lager = requests.post(create_lagers_in_basket_url, json.dumps(lager), headers=headers)
        print(requests_lager.json())


    def create_order(self):

        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json-patch+json"
        }

        order_field = {
            'customerPhone': "+380777777777",
            'ticketToken': "56",
            'filialId': 2382,
            'readyDate': '2019-07-31T20:00:00+03:00'
        }


        response = requests.post(create_order_url, json.dumps(order_field), headers=headers)

        print(response)

MyRequests().get_lagers()
