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
    return requests.get(BASE_URL + stock_symbol + QUOTE_URL).json()


# Return news regarding a company's stock
def get_stock_news(stock_symbol):
    # type: (String) -> json
    return requests.get(BASE_URL + stock_symbol + NEWS_URL).json()[0]

# Return long term stats of a company's stock
def get_stock_trendstats(stock_symbol):
    # type: (String) -> json
    return requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()


# Return key stats of a company's stock
def get_stock_keystats(stock_symbol):
    # type: (String) -> json
    return requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()


# Return price data of a company's stock
def get_stock_price(stock_symbol):
    # type: (String) -> float
    return requests.get(BASE_URL + stock_symbol + PRICE_URL).json()


# Return the stock ticker symbol of a company
def get_stock_symbol(company_name):
    request_url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en'.format(company_name)
    return requests.get(request_url).json()


# Resolve the slot name from the request
def get_resolved_value(request, slot_name):
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None
