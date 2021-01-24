1. Install dependecies: 
  pip install -r req.txt
2. start the server: 
  python app.py
  
example - 
curl --location --request POST 'http://localhost:5000/process_payment' \
--header 'Content-Type: application/json' \
--data-raw '{
    "card_number": "340653705597107",
    "card_holder": "Kanchan",
    "expiration_date": "03/2021",
    "security_code": "121",
    "amount": 1
}'
