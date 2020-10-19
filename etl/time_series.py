import requests
import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
import datetime
from pandas import json_normalize
import simplejson


class TimeSeries():
    def __init__(self, token, symbol):
        self.token = token
        self.symbol = symbol
        api_str = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+symbol+"&ouputsize=full&apikey="+token
        self.response = requests.get(api_str)
        return None

    def Run(self):
         print(self.response.json())

    def Stk_Analyze(self):
        self.stk_data = pd.DataFrame.from_dict(self.response.json()['Time Series (Daily)'], orient='index')
        self.symbol_col = [self.symbol] * len(self.stk_data)

        self.stk_data.columns = self.stk_data.columns.str[3:]
        self.stk_data['symbol_col'] = self.symbol_col
        self.stk_data.reset_index(inplace=True)
        self.stk_data.rename(columns={'index': 'date'}, inplace=True)

        print(self.stk_data)
        #self.stk_data.to_csv('stk_data')





def import_Timeseries():
    start_time =
    token = os.environ.get("api_key")
    symbol = "MSFT"
    p = TimeSeries(token=token, symbol=symbol)
    #p.Run()
    p.Stk_Analyze()


import_Timeseries()




