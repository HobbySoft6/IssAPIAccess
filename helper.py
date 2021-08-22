from constants import output_people, output_position, url_position, url_people
from Service.api_interface import retrieve_api_data
from Service.data_classes import Location, People

default_entity = output_position
"""
Generate requested strings for print out.
  : Param requested_entity: 
  : Return retrieved_info: Retrieve location or people information and covert it to python dict.  
"""


def output_result_string(requested_entity=default_entity):
    if requested_entity == output_people:
        retrieved_people = retrieve_api_data(url_people)
        people_dict = {}
        craft_set1 = set()
        for item in retrieved_people['people']:
            if item['craft'] not in craft_set1:
                craft_set1.add(item['craft'])
                people_dict[item['craft']] = [item['name']]
            else:
                people_dict[item['craft']].append(item['name'])
        current_people_string = People(people_dict)
        current_output_string = current_people_string

    else:
        retrieved_position = retrieve_api_data(url_position)
        latitude = retrieved_position['iss_position']['latitude']
        longitude = retrieved_position['iss_position']['longitude']
        timestamp = retrieved_position['timestamp']
        current_position_string = Location(latitude, longitude, timestamp)
        current_output_string = current_position_string
    return current_output_string


if __name__ == '__main__':
    #the_object = output_result_string(default_entity)
    the_object = output_result_string(output_people)
    print(the_object)