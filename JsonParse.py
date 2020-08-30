import json
from Person import *


# returns a list from a json file
def parse_json(file_name):
    ret = []  # store in a list
    file = open(file_name)

    # load JSON file
    people = json.load(file)  # list of dictionaries of data

    # store data in a Person object
    for p in people:
        ret.append(Person(p["ID"],
                          p["Name"],
                          p["Language"],
                          p["LovesShell"],
                          p["Hobbies"]))
    file.close()
    return ret
