import requests
import json
from ask_sdk_model import IntentRequest

# URLs for API requests
BASE_URL = "https://api.iextrading.com/1.0/stock/"
QUOTE_URL = "/quote?displayPercent=true"
NEWS_URL = "/news"
KEYSTATS_URL = "/stats"
PRICE_URL = "/price"

# Return a quote  for a company's stock
def get_stock_quote(stock_symbol):
    # type: (String) -> json
    quote_data = requests.get(BASE_URL + stock_symbol + QUOTE_URL).json()
    return_quote_data = {
        'symbol' : quote_data['symbol'],
        'name' : quote_data['companyName'],
        'sector' : quote_data['sector'],
        'primary_exchange' : quote_data['primaryExchange'],
        'open_price' : quote_data['open'],
        'current_price' : quote_data['calculationPrice'],
        'change_percentage' : quote_data['changePercent']        
    }
    return json.dumps(return_quote_data)

# Return news regarding a company's stock
def get_stock_news(stock_symbol):
    # type: (String) -> json
    news_data = requests.get(BASE_URL + stock_symbol + NEWS_URL).json()
    return_news_data = {
        'date' : news_data['datetime'],
        'title' : news_data['headline'],
        'source' : news_data['source'],
        'summary' : news_data['summary'] 
    }
    return json.dumps(return_news_data)

# Return key stats of a company's stock
def get_stock_keystats(stock_symbol):
    # type: (String) -> json
    keystats_data = requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()
    return_keystats_data = {
        'name': keystats_data['companyName'],
        'yearHigh' : keystats_data['week52high'],
        'yearLow' : keystats_data['week52low'],
        'yearChange' : keystats_data['week52change'],
        'latestEPS' : keystats_data['latestEPS'],
        'latestEPSDate' : keystats_data['latestEPSDate'],
        'peRatioHigh' : keystats_data['peRatioHigh'],
        'peRatioLow' : keystats_data['peRatioLow'],
        'priceToSale' : keystats_data['priceToSales'],
        'priceToBook' : keystats_data['priceToBook'],
        'day200MovingAvg' : keystats_data['day200MovingAvg'],
        'day50MovingAvg' : keystats_data['day50MovingAvg']
    }
    return json.dumps(return_keystats_data)

# Return price data of a company's stock
def get_stock_price(stock_symbol):
    # type: (String) -> json
    price_data = requests.get(BASE_URL + stock_symbol + PRICE_URL)
    return_price_data = {
        'price' : price_data['price']
    }
    return json.dumps(return_price_data)

# (INCORRECT, FIX!!) Return the stock ticker symbol of a company
def get_stock_symbol(company_Name):
    symbol = company_Name
    return symbol

# Resolve the slot name from the request
def get_resolved_value(request, slot_name):
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None