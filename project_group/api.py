from pathlib import Path
import csv
import requests
home = Path.home()
fp = Path.cwd()/"Cash on hand.csv"
fp.touch()
api_key = "8JYQTW7C6BBZ3SOQ"
function = "FX_WEEKLY"
from_currency = 'USD'
to_currency ='SGD'
url = f"https://www.alphavantage.co/query?function={function}&from_currency=USD&to_currency=SGD&apikey={api_key}"
r = requests.get(url)
data = r.json()
print(data)



