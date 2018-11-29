from __future__ import absolute_import
import requests, json

from decimal import Decimal, ROUND_HALF_UP

from ask_sdk_model import IntentRequest

from watson_develop_cloud import ToneAnalyzerV3

# URLs for API requests
BASE_URL = "https://api.iextrading.com/1.0/stock/"
SYMBOL_URL = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en"
QUOTE_URL = "/quote?displayPercent=true"
NEWS_URL = "/news"
KEYSTATS_URL = "/stats"
PRICE_URL = "/price"

# Return a quote  for a company's stock
def get_stock_quote(stock_symbol):
    # type: (String) -> json

    # Get quote
    quote_data = requests.get(BASE_URL + stock_symbol + QUOTE_URL).json()

    # Return quote
    return quote_data


# Return news regarding a company's stock
def get_stock_news(stock_symbol):
    # type: (String) -> json

    # Get news data
    news_data = requests.get(BASE_URL + stock_symbol + NEWS_URL).json()[0]

    # Return news
    return news_data


# Return key stats of a company's stock
def get_stock_keystats(stock_symbol):
    # type: (String) -> json

    # Get key stats
    key_stats = requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()

    # Return key stats
    return key_stats
    

# Return long term stats of a company's stock
def get_stock_trendstats(stock_symbol):
    # type: (String) -> json

    # Get trend stats 
    trend_stats = requests.get(BASE_URL + stock_symbol + KEYSTATS_URL).json()

    # Return trend stats
    return trend_stats


# Return price data of a company's stock
def get_stock_price(stock_symbol):
    # type: (String) -> float

    # Get stock price
    stock_price = requests.get(BASE_URL + stock_symbol + PRICE_URL).json()

    # Return price
    return stock_price


# Return the stock ticker symbol of a company
def get_stock_symbol(company_name):
    # type: (String) -> json

    # Get stock symbol
    request_url = SYMBOL_URL.format(company_name)
    stock_symbol = requests.get(request_url).json()

    # Return symbol
    return stock_symbol

def get_tone_analysis(summary_string):
    # type: (String) -> json

    # Tone Analyzer object
    tone_analyzer = ToneAnalyzerV3(
	                version = "2018-11-16",
	                iam_apikey = 'Insert API Key',
	                url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    )

    # Tone Analysis JSON
    tone_analysis = tone_analyzer.tone(tone_input = summary_string, content_type ='text/html')
    return tone_analysis
    

def get_decimal_value(decimal_value):
    # type: (Double) -> double

    # Format decimal value
    output_value = Decimal(decimal_value).quantize(Decimal('.01'), rounding = ROUND_HALF_UP)

    # Return formatted value
    return output_value


# Resolve the slot name from the request
def get_resolved_value(request, slot_name):
    # type: (IntentRequest, str) -> Union[str, None]
    try:
        # Return resolved value from slot
        return request.intent.slots[slot_name].value
        
    except (AttributeError, ValueError, KeyError, IndexError):
        # Return None
        return None
