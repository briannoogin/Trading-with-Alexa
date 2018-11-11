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
    return quote_data

# Return news regarding a company's stock
def get_stock_news(stock_symbol):
    # type: (String) -> json
    news_data = requests.get(BASE_URL + stock_symbol + NEWS_URL).json()
    return news_data

# Return key stats of a company's stock
def get_stock_keystats(stock_symbol):
    # type: (String) -> json
    keystats_data = requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()
    return keystats_data

# Return long term stats of a company's stock
def get_stock_trendstats(stock_symbol):
    # type: (String) -> json
    trendstats_data = requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()
    return trendstats_data
    
# Return price data of a company's stock
def get_stock_price(stock_symbol):
    # type: (String) -> json
    price_data = requests.get(BASE_URL + stock_symbol + PRICE_URL).json()
    return price_data

# (INCORRECT, FIX!!) Return the stock ticker symbol of a company
def get_stock_symbol(company_Name):
    symbol = "AAPL"
    return symbol

# Resolve the slot name from the request
def get_resolved_value(request, slot_name):
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        return request.intent.slots[slot_name].value
    except (AttributeError, ValueError, KeyError, IndexError):
        return None