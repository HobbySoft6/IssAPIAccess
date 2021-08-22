# IssAPIAccess
Integrate with Iss API to retrieve craft location and people information

Modules and file include:
  . iss_main.py: The main file to run this project.
  . constants.py: The constants such as urls of APIs and others to support this project.
  . helper.py: With a function output_result_string() to retrieve ISS API data, and transfer to
    desired format for print out.
  . Service: A python package which includes the modules: api_interface.py, and data_calsses.py
  . api_interface.py: A interface with a function retrieve_api_data() to directly get ISS APIs
    data based on the input url.
  . data_classes.py: there are two classes: Location and People. Variables are passed to the classed
    by creating objects. objects are converted to right format strings using __str__ method.
  . requirements.txt: includes python packages are required to run the project.

To run this project:
  . Install python
  . Setting python path
  . Install the project dependency: requests 
  . from the terminal to run command:
    >python iss_main.py arg(s)
    choose one or two args from followings:
    arg1: "for each craft print the details of those people that are currently in space"
    arg1 to pull and output craft(s) and people information.
    arg2:  "print the current location of the ISS"
    arg2 to pull and output ISS location information.
  . run command example:
    a. output only ISS location:
       > python iss_main.py "print the current location of the ISS" 
    b. output only craft(s) and People:
       > python iss_main.py "for each craft print the details of those people that are currently in space"
    c. output both location and craft(s) and People:
       > python iss_main.py "print the current location of the ISS" "for each craft print the details of those
         people that are currently in space"
