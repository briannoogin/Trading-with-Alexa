# Simple program to make a python API request and return the status code
import requests

# The base url for the IEX API is https://api.iextrading.com/1.0, and we will be accessing the stocks
# endpoint (/stocks/) so we'll add this to the beginning of all of our endpoints.
base_url = 'https://api.iextrading.com/1.0/stock/'
stock_symbol = input("What stock symbol would you like to get the price for? ").upper()

# Make a GET request to get the latest price of the stock of any company, given the stock symbol
response = requests.get(base_url + stock_symbol + '/price/')
response_dict = response.json()
print("The price of " + stock_symbol + " is $" + str(response_dict))


