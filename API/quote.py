import requests
import json


def lambda_handler(event, context):
    base_url = "https://api.iextrading.com/1.0/stock/"
    stock_symbol = event['key_url']
    response = requests.get(base_url + stock_symbol + '/quote/?displayPercent=true')
    json_data = json.loads(response.text)
    json_return_data = {}
    json_return_data['Symbol'] = json_data['symbol']
    json_return_data['Company Name'] = json_data['companyName']
    json_return_data['Sector'] = json_data['sector']
    json_return_data['Primary Exchange'] = json_data['primaryExchange']
    json_return_data['Opening Price:'] = json_data['open']
    json_return_data['Change Percentage'] = json_data['changePercent']
    json_stuff = json.dumps(json_return_data)
    print(json_stuff)
    #return json_stuff







