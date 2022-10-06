from flask import Flask, render_template, Response , request, jsonify
import socket
from data_validator import payment_data_validator
from payment_methode import Payment
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/process_payment/', methods=['POST'])
def ProcessPayment():
    data_received = json.loads(request.data.decode()[1:-1])
    if 'security_code' in  data_received.keys():
        data = [{
            'credit_card_number':data_received['credit_card_number'],
            'card_holder':data['card_holder'],
            'expiration_date':datetime.strptime(data_received['expiration_date'], '%Y-%m-%d'),
            'security_code':data_received['security_code'],
            'amount':data_received['amount']
        },]
    else:
        data = [{
            'credit_card_number':data_received['credit_card_number'],
            'card_holder':data_received['card_holder'],
            'expiration_date':datetime.strptime( data_received['expiration_date'], '%Y-%m-%d'),
            'amount':data_received['amount']
        },]
    try:
        assert payment_data_validator.validate(data)
    except: 
        response = app.response_class(
            response=json.dumps("invalid request"),
            status=400,
            mimetype='application/json'
        )
        return response
    payment = Payment()
    payment.get_payment_methode(data_received['amount'])
    response = payment.proceed_payment(data)
    if response.status_code == 200:
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    
    if response.status_code == 400:
        response = app.response_class(
            response=json.dumps('the request is invalid'),
            status=400,
            mimetype='application/json'
        )
        return response

    response = app.response_class(
            response=json.dumps('internal server error'),
            status=500,
            mimetype='application/json'
        )
    return response 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

# curl --header "Content-Type: application/json" \
#   --request POST \
#   --data '{'credit_card_number':'5123-1231-2332-1565','card_holder':'khaledha','expiration_date':d1,'amount':50}' \
#   http://0.0.0.0:8080/process_payment
