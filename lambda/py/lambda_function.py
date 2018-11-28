# Import relevant modules
import json
import logging
from datetime import datetime


from alexa import data, util
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response


# Skill Builder Object
skill = SkillBuilder()


# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-In Intent Handlers
class LaunchRequestHandler(AbstractRequestHandler):
    # Handler for Skill Launch
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In LaunchRequestHandler")

        # Return welcome response
        handler_input.response_builder.speak(data.WELCOME_MESSAGE).set_should_end_session(False)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    # Handler for Help Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        # Resetting the session
        handler_input.attributes_manager.session_attributes = {}

        # Return help response
        handler_input.response_builder.speak(data.HELP_MESSAGE).ask(data.HELP_PROMPT).set_should_end_session(False)
        return handler_input.response_builder.response


class ExitIntentHandler(AbstractRequestHandler):
    # Handler for Cancel, Pause, or Stop Intents
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.PauseIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In ExitIntentHandler")

        # Return stop response
        handler_input.response_builder.speak(data.STOP_MESSAGE).set_should_end_session(True)
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    # Handler for Fallback Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        logger.info("In FallbackIntentHandler")

        # Return fallback response
        handler_input.response_builder.speak(data.FALLBACK_MESSAGE).ask(data.FALLBACK_PROMPT).set_should_end_session(False)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    # Handler for Session End
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Log reason for end session
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended reason: {}".format(handler_input.request_envelope.request.reason))

        # Return session ended reason response
        return handler_input.response_builder.response


class CatchAllExceptionsHandler(AbstractExceptionHandler):
    # Handler for all Exceptions
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, exception) -> Response

        # Log exceptions
        logger.info("In CatchAllExceptionsHandler")
        logger.error(exception, exc_info=True)

        # Return exception message
        handler_input.response_builder.speak(data.EXCEPTION_MESSAGE).ask(data.HELP_PROMPT)
        return handler_input.response_builder.response


# Custom Intent Handlers
class QuoteIntentHandler(AbstractRequestHandler):
    # Handler for Quote Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("QuoteIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetQuoteHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result'][0]['symbol']

        # Get quote using retrieved symbol
        quote = util.get_stock_quote(symbol)

        logger.debug("Got stock quote for {}".format(company))

        # Format values from quote
        open_price = util.get_decimal_value(quote['open'])
        latest_price = util.get_decimal_value(quote['latestPrice'])
        change_percent = util.get_decimal_value(quote['changePercent'])

        # Create message for quote
        message = data.QUOTE_MESSAGE.format(quote['symbol'], quote['companyName'], quote['sector'], quote['primaryExchange'],
                                            open_price, latest_price, change_percent)

        # Return message for quote
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response


class NewsIntentHandler(AbstractRequestHandler):
    # Handler for News Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        test = is_intent_name("NewsIntent")(handler_input)
        logger.debug("The value of is_intent_name is {}".format(test))
        return is_intent_name("NewsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewsHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result'][0]['symbol']

        # Get stock news using symbol
        news = util.get_stock_news(symbol)
        logger.debug("Got stock news of {}".format(company))

        # Get tone analysis using news summary
        tone_analysis = util.get_tone_analysis(news['summary'])
        json_tones = json.loads(str(tone_analysis))
        logger.debug("Got tone analysis of {}".format(company))

        # Create message for tone
        tone_message = ''
        for tone in json_tones['document_tone']['tones']:
            percent_confidence = util.get_decimal_value(tone['score'] * 100)
            tone_name = tone['tone_name']
            tone_message += data.TONE_MESSAGE.format(percent_confidence, tone_name)

        # Create message for news
        message = data.NEWS_MESSAGE.format(news['headline'], news['source'], news['datetime'], tone_message)

        # Return message for news
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response


class KeyStatsIntentHandler(AbstractRequestHandler):
    # Handler for Key Stats Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("KeyStatsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetKeyStatHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result'][0]['symbol']

        # Get key stats data using symbol
        key_stats = util.get_stock_keystats(symbol)

        logger.debug("Got key stats of {}".format(company))

        # Format values from key_stats
        week52_high = util.get_decimal_value(key_stats['week52high'])
        week52_low = util.get_decimal_value(key_stats['week52low'])
        week52_change = util.get_decimal_value(key_stats['week52change'])
        latest_EPS = util.get_decimal_value(key_stats['latestEPS'])
        peRatio_high = util.get_decimal_value(key_stats['peRatioHigh'])
        peRatio_low = util.get_decimal_value(key_stats['peRatioLow'])
        price_sales = util.get_decimal_value(key_stats['priceToSales'])
        price_book = util.get_decimal_value(key_stats['priceToBook'])
        day200_mAvg = util.get_decimal_value(key_stats['day200MovingAvg'])
        day50_mAvg = util.get_decimal_value(key_stats['day50MovingAvg'])

        # Create message for key stats
        message = data.KEYSTATS_MESSAGE.format(key_stats['companyName'], week52_high, week52_low,
                                               week52_change, latest_EPS, key_stats['latestEPSDate'], 
                                               peRatio_high, peRatio_low, price_sales, price_book,
                                               day200_mAvg, day50_mAvg)

        # Return key stats response
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response


class TrendStatsIntentHandler(AbstractRequestHandler):
    # Handler for Trend Stats Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("TrendStatsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In TrendStatsHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result']['0']['symbol']

        # Get trend stats using symbol
        trend_stats = util.get_stock_trendstats(symbol)

        logger.debug("Got trend stats of {}".format(company))

        # Format trend_stats values
        week52_high = util.get_decimal_value(trend_stats['week52high'])
        week52_low = util.get_decimal_value(trend_stats['week52low'])
        week52_change = util.get_decimal_value(trend_stats['week52change'])
        ebitda = util.get_decimal_value(trend_stats['EBITDA'])
        day200_mAvg = util.get_decimal_value(trend_stats['day200MovingAvg'])
        day50_mAvg = util.get_decimal_value(trend_stats['day50MovingAvg'])
        year5_change = util.get_decimal_value(trend_stats['year5ChangePercent'])
        year2_change = util.get_decimal_value(trend_stats['year2ChangePercent'])
        year1_change = util.get_decimal_value(trend_stats['year1ChangePercent'])
        month6_change = util.get_decimal_value(trend_stats['month6ChangePercent'])
        month3_change = util.get_decimal_value(trend_stats['month3ChangePercent'])
        month1_change = util.get_decimal_value(trend_stats['month1ChangePercent'])
        day5_change = util.get_decimal_value(trend_stats['day5ChangePercent'])

        # Create key stats message
        message = data.TRENDSTATS_MESSAGE.format(trend_stats['companyName'], week52_high, week52_low, 
                                                 week52_change, ebitda,day200_mAvg, day50_mAvg, year5_change,
                                                 year2_change, year1_change, month6_change, month3_change,
                                                 month1_change, day5_change)
        
        # Return trend stats response
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response


class PriceIntentHandler(AbstractRequestHandler):
    # Handler for Price Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("PriceIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetPriceHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result'][0]['symbol']

        # Get stock price using symbol
        price = util.get_stock_price(symbol)

        logger.debug("Got price of {}".format(company))

        # Create message for price
        message = data.PRICE_MESSAGE.format(company, price)

        # Return price response
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response
        

class BuyIntentHandler(AbstractRequestHandler):
    # Handler for Buy Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BuyIntent")(handler_input)
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In BuyIntentHandler")

        # Get user's input for company slot from Alexa
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")
        quantity = util.get_resolved_value(handler_input.request_envelope.request, "quantity")

        # Get stock symbol of company
        s = util.get_stock_symbol(company)
        symbol = s['ResultSet']['Result'][0]['symbol']

        # Get stock price using symbol
        price = util.get_stock_price(symbol)

        # Create message for stock bought
        message = data.BUY_MESSAGE.format(quantity, company, price, datetime.today())

        # Return buy response
        handler_input.response_builder.speak(message).set_should_end_session(False)
        return handler_input.response_builder.response


class RequestLogger(AbstractRequestInterceptor):
    # Log Alexa Requests
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    # Log Alexa Responses
    def process(self, handler_input, response):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register all request handlers to the skill
skill.add_request_handler(LaunchRequestHandler())
skill.add_request_handler(QuoteIntentHandler())
skill.add_request_handler(NewsIntentHandler())
skill.add_request_handler(KeyStatsIntentHandler())
skill.add_request_handler(PriceIntentHandler())
skill.add_request_handler(TrendStatsIntentHandler())
skill.add_request_handler(BuyIntentHandler() )
skill.add_request_handler(HelpIntentHandler())
skill.add_request_handler(FallbackIntentHandler())
skill.add_request_handler(ExitIntentHandler())
skill.add_request_handler(SessionEndedRequestHandler())

# Register exception handler to the skill
skill.add_exception_handler(CatchAllExceptionsHandler())

# Initiate response and request logs
skill.add_global_request_interceptor(RequestLogger())
skill.add_global_response_interceptor(ResponseLogger())

# Register lambda handler in AWS Lambda
lambda_handler = skill.lambda_handler()