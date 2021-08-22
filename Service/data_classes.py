from dataclasses import dataclass


# dataclass for position or location of the ISS
@dataclass
class Location:
    latitude: str
    longitude: str
    timestamp: int

    def __str__(self):
        return   f'The ISS current location at {self.timestamp} is {{{self.latitude}, {self.longitude}}}'


"""
the following dataclass is for people on craft(s)
  . variable people_dict: it is a dictionary with keys are crafts and values are lists. 
    The lists include names who are within the corresponding crafts. 
"""


@dataclass
class People:
    people_dict: dict

    def __str__(self):
        current_people = f''
        for key, value in self.people_dict.items():
            name_string = f''
            for item in value:
                if name_string == '':
                    name_string = f'{item}'
                else:
                    name_string = name_string + f', ' + f'{item}'
            if current_people == '':
                current_people = f'There are {len(value)} people aboard the {key}, They are {name_string}.'
            else:
                current_people = current_people + f'\nThere are {len(value)} people aboard the {key}, They are {name_string}.'
        return current_people


if __name__ == '__main__':
    the_location = Location('29.9799', '-84.9591', 1629572576)
    print(the_location)
    the_people_dict = {'ISS': ['Mark Vande Hei', 'Oleg Novitskiy', 'Pyotr Dubrov', 'Thomas Pesquet', 'Megan McArthur', 'Shane Kimbrough', 'Akihiko Hoshide'], 'Tiangong': ['Nie Haisheng', 'Liu Boming', 'Tang Hongbo']}
    the_people = People(the_people_dict)
    print(the_people)


