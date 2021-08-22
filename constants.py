# urls for the APIs
url_position = "http://api.open-notify.org/iss-now.json"
url_people = "http://api.open-notify.org/astros.json"

# mock data for that APIs are not available
mock_position = {'iss_position': {'longitude': '134.8304', 'latitude': '-51.3972'}, 'message': 'success', 'timestamp': 1629546626}
mock_people = {'people': [{'name': 'Mark Vande Hei', 'craft': 'ISS'}, {'name': 'Oleg Novitskiy', 'craft': 'ISS'}, {'name': 'Pyotr Dubrov', 'craft': 'ISS'}, {'name': 'Thomas Pesquet', 'craft': 'ISS'}, {'name': 'Megan McArthur', 'craft': 'ISS'}, {'name': 'Shane Kimbrough', 'craft': 'ISS'}, {'name': 'Akihiko Hoshide', 'craft': 'ISS'}, {'name': 'Nie Haisheng', 'craft': 'Tiangong'}, {'name': 'Liu Boming', 'craft': 'Tiangong'}, {'name': 'Tang Hongbo', 'craft': 'Tiangong'}], 'number': 10, 'message': 'success'}

# command line arguments
command_position = "print the current location of the ISS"
command_people = "for each craft print the details of those people that are currently in space"

# indicators for different output data
output_position = "object_position"
output_people = "object_people"


if __name__ == '__main__':
    print(mock_position)
    print(mock_position["timestamp"])
    print(mock_people)
    print(mock_people["number"])