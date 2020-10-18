import requests
import os
from dotenv import load_dotenv
load_dotenv()
import simplejson

class Fundamentals():
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol
        api_str = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+symbol+"&apikey="+token
        self.response = requests.get(api_str)
        return None

    def run(self):
         print(self.response.json())


def import_fundamentals():
    token = os.environ.get("api_key")
    symbol = "MSFT"
    p = Fundamentals(token=token, symbol=symbol)
    p.run()


import_fundamentals()
