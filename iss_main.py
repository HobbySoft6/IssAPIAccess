import sys
from helper import output_result_string
from constants import output_people, output_position

current_people_string = output_result_string(output_people)
current_position_string = output_result_string(output_position)

if len(sys.argv) == 2:
    arg1_normal = sys.argv[1].lower()
    people_keywords_list = ['craft', 'people']
    if any(x in arg1_normal for x in people_keywords_list):
        result_string = current_people_string
    else:
        result_string = current_position_string
else:
    current_position_people_string = str(current_position_string) + f'\n' + str(current_people_string)
    result_string = current_position_people_string
print(result_string)
