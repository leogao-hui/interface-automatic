#_author:LEO GAO
#_project Encoding: UTF-8

import requests
from Common.data import data
from Common.config import header
from Common.apiUrl.accountController.accountControllerUrl import login_with_pw_url

class AccountControllerFunction:

    def login_with_password(self):
        request = requests.session()
        response = request.post(headers=header, url=login_with_pw_url, data=data)
        return response.status_code

