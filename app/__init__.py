import json
from flask import Flask
from liqpay.liqpay import LiqPay


app = Flask(__name__)
app.config.update(
    SECRET_KEY='paymentApp',
    public_key='sandbox_i94968495390',
    private_key='sandbox_HZbL5RIZb15TCoPxSCfgrABCszPR9dEU39uifIIg'
)

lp = LiqPay(
    app.config.get('public_key'),
    app.config.get('private_key')
)

payments = {}

with open('./app/rooms.json', 'r') as f:
    rooms = json.load(f)


from app import routes
