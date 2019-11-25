# author:LEO GAO
# project Encoding:UTF-8


import configparser
import os
import json

first = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
case_path = os.path.join(first, "config.ini")
config = configparser.ConfigParser()
config.read(case_path)
ci_url = config.get("url", "backend_url")[1:-1]

header = {}
# stYPz8KmQtOjWz0nSXXjiOTdATOLtnNGf1pEumZlsd+dmxpCarFr8S+P6KF7+/Nd

def get_header(authorization):
    header = {"Content-Type": "application/json", "charset": "UTF-8", "Authorization": authorization}
    return header


def json_dump(data):
    json_data = json.dumps(data)
    return json_data


def println(status, value):
    if status == 1:
        print('\033[34m%s is pass' % value)
    elif status == 2:
        print('\033[31m%s is fail' % value)
