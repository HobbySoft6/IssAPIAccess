import sys
from helper import output_result_string
from constants import output_people, output_position

# retrieve and generate the required output strings
current_people_string = output_result_string(output_people)
current_position_string = output_result_string(output_position)
"""
the main module to run the project.
  for example:
    from terminal to run: C:\\Users\\xxx\\IdeaProjects\\IssAPIAccess> python iss_main.py "for each craft print the
                          details of those people that are currently in space"
The basic command line arguments logic:
  . If there is only one argument, check if it requires craft and people. If it is not, output location information.
  . if there is no any argument or more than 1 argument, output both location and craft and people information. 
"""
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


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))