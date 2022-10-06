from schema import Schema, And, Use, Optional, SchemaError
import re
from datetime import datetime

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def check_credit_card(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9) or hyphens '-',
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    """

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

    for group in match.groups():
        if group[0] * 4 == group:
            return False
    return True

def check_expiration_date(expiration_date):
    today = datetime.today()
    if expiration_date < today:
        return False
    return True 

payment_data_validator = Schema([{   'credit_card_number': And(str,check_credit_card),
                                'card_holder':  And(str,Use(str)),
                                'expiration_date': And(datetime.date,check_expiration_date),
                                Optional('security_code'): And(str,lambda n: len(n)==3),
                                'amount':  And(Use(int), lambda n: 0 <= n ) }])

if __name__ == "__main__":
    d1 = datetime(2022, 5, 3)
    data = [{
            'credit_card_number':'5123-1231-2332-1565',
            'card_holder':'khaledha',
            'expiration_date':d1,
            'amount':50
        },]
    # print(data)
    ok = payment_data_validator.validate(data)
    print(ok)