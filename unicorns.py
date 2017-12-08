import os
import pandas
import apikeys
import requests as req
import json
url = "https://www.alphavantage.co/query?"
params = {'apikey': apikeys.ALPHA_VANTAGE_KEY,
          'function': 'TIME_SERIES_DAILY_ADJUSTED',
          'symbol': 'AAPL',
          'outputsize': 'full'}
respadjusted = req.get(url, params=params).json()
print(json.dumps(respadjusted, indent=4, sort_keys=True))
