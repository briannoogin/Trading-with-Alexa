# Standard Alexa Messages
SKILL_NAME = "Stock Informing"
WELCOME_MESSAGE = "Welcome to Sock Informing with Alexa! "
"This skill helps inform the user of the current state of "
"a company's stock."
QUOTE_MESSAGE = (
    "Here's your quote: "
    "The stock symbol is {}. "
    "The company name is {}. "
    "It is in the {} sector. "
    "The primary exchange is {}. "
    "Opening price was ${}. "
    "The current price is ${}. "
    "The percent change from previous closing price is {}. "
    )
NEWS_MESSAGE = (
    "Here's the news: "
    "Dated {}. "
    "The headline is: {}. "
    "Sourced by {}. "
    "Here's a summary: {}."
    )
KEYSTATS_MESSAGE = (
    "Here are the key stats: "
    "The company name is {}. "
    "The year highs and lows are ${} and ${} respectively. "
    "The yearly change in price is {}%. "
    "Latest earnings per share is ${} as of {}. "
    "The price to earnings ratio highs and lows are {} and {} respectively. "
    "The price to book ratio is {} and the price to sales ratio is {}. "
    "The day 200 moving average is ${}. "
    "The day 50 moving average is ${}. "
    )
PRICE_MESSAGE = (
    "The current stock price for {} is ${}."
    )
HELP_MESSAGE  = "You can ask me to give you a quote, news, key stats, and/or price on a company's stock. Or you can say exit."
HELP_PROMPT = "What can I help you with?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "The Stock Informing skill can't help with that. It can inform you on varying levels of information on a company's stock"
FALLBACK_PROMPT = "What can I help you with?"
EXCEPTION_MESSAGE  = "Sorry. I cannot help you with that."