from etl.fundamentals import Fundamentals
import os


def import_fundamentals():
    token = os.environ.get("api_key")
    symbol = "MSFT"
    p = Fundamentals(token=token, symbol=symbol)
    p.run()


import_fundamentals()