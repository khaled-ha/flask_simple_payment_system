import requests as req
from requests import post
from json     import dumps

class BaseAPI(object):
    DEFAULT_HEADERS = {'content-type': 'application/json','accept': 'application/json'}
    def send_api_request(self, url, data):
        return post(
            url     = url,
            data    = dumps(data),
            timeout = 120,
            headers = self.DEFAULT_HEADERS,
            verify  = True,
        )

class PremuimPaymentGateway(BaseAPI):
    def __init__(self):
        self.post_url = 'http://payment:8000/api/premuim_payement_gateway/'
        self.data_to_post = []

    def post_payment(self,data):
        self.data_to_post = data
        response = self.send_api_request(url=self.post_url,data=self.data_to_post)
        return response

class ExpensivePaymentGateway(BaseAPI):
    def __init__(self):
        self.post_url = 'http://payment:8000/api/expensive_payement_gateway/'
        self.data_to_post = []

    def post_payment(self,data):
        self.data_to_post = data
        response = self.send_api_request(url=self.post_url,data=self.data_to_post)
        return response

class CheapPaymentGateway(BaseAPI):
    def __init__(self):
        self.post_url = 'http://payment:8000/api/cheap_payement_gateway/'
        self.data_to_post = []

    def post_payment(self,data):
        self.data_to_post = data
        response = self.send_api_request(url=self.post_url,data=self.data_to_post)
        return response


class Payment:
    def __init__(self):
        self.payment_methode = None
        self.number_of_tries = None

    def get_payment_methode(self,amount):

        if amount < 20:
            self.payment_methode =  CheapPaymentGateway
        if (amount >= 21) and (amount <= 500):
            self.payment_methode = ExpensivePaymentGateway
            self.number_of_tries = 1
        if amount > 500:
            self.number_of_tries = 3
            self.payment_methode = PremuimPaymentGateway 
 
    def proceed_payment(self,data):
        payment = self.payment_methode()
        data[0]['expiration_date'] = data[0]['expiration_date'].strftime('%Y-%m-%d')
        response = payment.post_payment(data)

        if response.status_code != 200 and  isinstance(payment , ExpensivePaymentGateway) :
            payment = CheapPaymentGateway()
            payment.post_payment(data)
        
        if response.status_code != 200 and isinstance(payment , PremuimPaymentGateway):
            for x in range(3):
                payment.post_payment(data)

        return response
