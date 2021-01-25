valid_american_express_input = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "123",
    "amount": 2
}

valid_visa_card = {
    "card_number": "4929248980295542",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "123",
    "amount": 2
}

valid_master_card = {
    "card_number": "5303765013600904",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "123",
    "amount": 2
}

valid_master_card = {
    "card_number": "5303765013600904",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "123",
    "amount": 2
}

invalid_card = {
    "card_number": "990653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/202",
    "security_code": "123",
    "amount": 2
}

card_holder_missing = {
    "card_number": "340653705597107",
    "expiration_date": "08/2021",
    "security_code": "123",
    "amount": 2
}

expiration_date_in_past = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/2020",
    "security_code": "123",
    "amount": 2
}

security_code_missing = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "amount": 2
}

invalid_security_code = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "13",
    "amount": 2
}

amount_missing = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date": "08/2021",
    "security_code": "123"
}

invalid_amount = {
    "card_number": "340653705597107",
    "card_holder": "test_user",
    "expiration_date":"08/2021",
    "security_code": "123",
    "amount": 0
}