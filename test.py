

import unittest
import requests
import json

url = 'http://193.112.184.109:8007/account/check-captcha'

header = {"Content-Type": "application/json", "charset": "UTF-8"}

data_phone = json.dumps({
    'phoneNum': '18721270883',
    'captcha': '945125'
})

response = requests.post(url=url, headers=header, data=data_phone)
print(response.json(), response.status_code)


