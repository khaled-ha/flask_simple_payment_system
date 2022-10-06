import requests as req
from requests import post
from json     import dumps
from datetime import datetime
from app.payment_methode import BaseAPI

data1 = [{
            'credit_card_number':'5123-1231-2332-1565',
            'card_holder':'khaledha',
            'expiration_date':'2020-12-5',
            'amount':5000
        },]

data2 = [{
            'credit_card_number':'5123-1231-2332-1565',
            'card_holder':'khaledha',
            'expiration_date':'2022-12-5',
            'amount':5
        },]
data3 = [{
            'credit_card_number':'5123-1231-2332-1565',
            'card_holder':'khaledha',
            'expiration_date':'2022-12-5',
            'amount':5000
        },]

data4 = [{
            'credit_card_number':'5123-1231-2332-1565',
            'card_holder':'khaledha',
            'expiration_date':'2022-12-5',
            'amount':50
        },]

if __name__ == "__main__":
    test_api = BaseAPI()
    for x in [data1,data2,data3,data4]:
        response = test_api.send_api_request(url='http://0.0.0.0:8080/process_payment/',data=x)
    print(response)