import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json

class Fundamentals():
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol
        api_str = "https://www.alphavantage.co/query?function=OVERVIEW&symbol="+symbol+"&apikey="+token
        self.response = requests.get(api_str)
        return None

    def run(self):
        return print(self.response.json())

