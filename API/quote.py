import requests
import json


def lambda_handler(event, context):
    base_url = "https://api.iextrading.com/1.0/stock/"
    stock_symbol = event['symbol']

    json_data = requests.get(base_url + stock_symbol + '/quote/?displayPercent=true').json()
    print(json_data)
    json_return_data = {
        'Symbol': json_data['symbol'],
        'Company Name': json_data['companyName'],
        'Sector': json_data['sector'],
        'Primary Exchange': json_data['primaryExchange'],
        'Opening Price:': json_data['open'],
        'Change Percentage': json_data['changePercent']
    }
    print(json.dumps(json_return_data))
    return json.dumps(json_return_data)







