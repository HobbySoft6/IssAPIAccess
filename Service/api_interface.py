import requests
from requests.exceptions import Timeout
import constants
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

default_url = constants.url_position
"""
Retrieve location and/or people data through ISS APIs.
  : Param input_url: the url where data are pulled from. Since there are two URLs, the location url is sed as default.
  : Return retrieved_info: Retrieve location or people information and covert it to python dict.  
"""


def retrieve_api_data(input_url=default_url):
    retrieved_info = ''
    try:
        resp = requests.get(input_url, timeout=3)
        retrieved_info = json.loads(resp.text)
    except requests.exceptions.ConnectionError as e:
        logger.error(f"ConnectionError: {e}")
    # provide mock data if endpoints are not available
    except Timeout as e:
        if input_url == constants.url_people:
            retrieved_info = constants.mock_people
        else:
            retrieved_info = constants.mock_position
        logger.warning(f"Timeout: {e}")
    return retrieved_info


if __name__ == '__main__':
    #position
    result_position = retrieve_api_data(constants.url_position)
    print(result_position)
    latitude = result_position['iss_position']['latitude']
    print(latitude)
    longitude = result_position['iss_position']['longitude']
    print(longitude)
    timestamp = result_position['timestamp']
    print(timestamp)
    print(f'The ISS current location at {timestamp} is {{{latitude}, {longitude}}}')

    #people
    result_people = retrieve_api_data(constants.url_people)
    print(result_people)
    result_dict = {}
    craft_set1 = set()
    for item in result_people['people']:
        if item['craft'] not in craft_set1:
            craft_set1.add(item['craft'])
            result_dict[item['craft']] = [item['name']]
        else:
            result_dict[item['craft']].append(item['name'])
    print('result_dict:')
    print(result_dict)
    output_string = f''
    for key, value in result_dict.items():
        name_string = f''
        for item in value:
            if name_string == '':
                name_string = f'{item}'
            else:
                name_string = name_string + f', ' + f'{item}'
        if output_string == '':
            output_string = f'There are {len(value)} people aboard the {key}, They are {name_string}. '

        else:
            output_string = output_string + f'\nThere are {len(value)} people aboard the {key}, They are {name_string}. '
        print(value)
    print(output_string)





