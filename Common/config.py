# author:LEO GAO
# project Encoding:UTF-8


import configparser
import os

first = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
case_path = os.path.join(first, "config.ini")
config = configparser.ConfigParser()
config.read(case_path)
ci_url = config.get("url", "backend_url")[1:-1]
print(ci_url)

header = {"Content-Type": "application/json", "charset": "UTF-8"}


def println(status, value):
    if status == 1:
        print('\033[34m%s is pass' % value)
    elif status == 2:
        print('\033[31m%s is fail' % value)
