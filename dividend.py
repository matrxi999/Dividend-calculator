import requests

def get_div_value(symbol):
    
    url = "https://api.polygon.io/v2/reference/dividends/"+ symbol + "?apiKey=_O3GJ5qwhPDU9QYsxIcb9yIq3S2KOtDf"

    response = requests.get(url)

    return response.json()['results'][0]['amount']