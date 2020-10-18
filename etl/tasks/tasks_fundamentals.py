from etl import fundamentals
import os
from dotenv import load_dotenv
load_dotenv()

def import_fundamentals():
    token = os.environ.get("api_key")
    symbol = "MSFT"
    p = Fundamentals(token=token, symbol=symbol)
    p.run()
