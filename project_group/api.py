from pathlib import Path
import csv
import requests, json, re
home = Path.home()
fp = Path.cwd()/"Cash on hand.csv"
fp.touch()
api_key = "8JYQTW7C6BBZ3SOQ"
function = "CURRENCY_EXCHANGE_RATE"
from_currency = 'USD'
to_currency ='SGD'
url = f"https://www.alphavantage.co/query?function={function}&from_currency=USD&to_currency=SGD&apikey={api_key}"
r = requests.get(url)
data = r.json()
data = json.dumps(data,indent=4)

data = re.search('Exchange Rate": ".+',data)
data = data.group(0)
print(data.strip('Exchange Rate":"",'))




