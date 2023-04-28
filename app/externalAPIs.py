import requests

def fetchLatestBitcoinPrice():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url=url)
    return response