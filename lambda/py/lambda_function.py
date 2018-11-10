# Import relevant modules
import json
import logging
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
        handler_input.response_builder.speak(data.WELCOME_MESSAGE)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    # Handler for Help Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")
        handler_input.response_builder.speak(data.HELP_MESSAGE).ask(data.HELP_PROMPT)
        return handler_input.response_builder.response

class CancelorStoporPauseIntentHandler(AbstractRequestHandler):
    # Handler for Cancel, Pause, or Stop Intents
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or 
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.PauseIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelorStoporPauseIntentHandler")
        handler_input.response_builder.speak(data.STOP_MESSAGE)
        return handler_input.response_builder.response

class FallbackIntentHandler(AbstractRequestHandler):
    # Handler for Fallback Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> response
        logger.info("In FallbackIntentHandler")
        handler_input.response_builder.speak(data.FALLBACK_MESSAGE).ask(data.FALLBACK_PROMPT)
        return handler_input.response_builder.response

class SessionEndedRequestHandler(AbstractRequestHandler):
    # Handler for Session End
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended reason: {}".format(handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response

class CatchAllExceptionsHandler(AbstractExceptionHandler):
    # Handler for all Exceptions
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, exception) -> Response
        logger.info("In CatchAllExceptionsHandler")
        logger.error(exception, exc_info = True)
        handler_input.response_builder.speak(data.EXCEPTION_MESSAGE).ask(data.HELP_PROMPT)
        return handler_input.response_builder.response

# Custom Intent Handlers
class GetQuoteHandler(AbstractRequestHandler):
    # Handler for Quote Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("QuoteIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetQuoteHandler")
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")
        symbol = util.get_stock_symbol(company)
        quote = util.get_stock_quote(symbol)
        message = data.QUOTE_MESSAGE.format(quote['symbol'], quote['name'], quote['sector'], quote['primary_exchange'], 
            quote['open_price'], quote['current_price'], quote['change_percentage'])
        handler_input.response_builder.speak(message)
        return handler_input.response_builder.response

class GetNewsHandler(AbstractRequestHandler):
    # Handler for News Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("NewsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewsHandler")
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")
        symbol = util.get_stock_symbol(company)
        news = util.get_stock_news(symbol)
        message = data.NEWS_MESSAGE.format(news['date'], news['title'], news['source'], news['summary'])
        handler_input.response_builder.speak(message)
        return handler_input.response_builder.response

class GetKeyStatHandler(AbstractRequestHandler):
    # Handler for Key Stats Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("KeyStatsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetKeyStatHandler")
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")
        symbol = util.get_stock_symbol(company)
        key_stats = util.get_stock_keystats(symbol)
        message = data.KEYSTATS_MESSAGE.format(key_stats['name'], key_stats['yearHigh'], key_stats['yearLow'],
            key_stats['yearChange'], key_stats['latestEPS'], key_stats['latestEPSDate'], key_stats['peRatioHigh'],
            key_stats['peRatioLow'], key_stats['priceToSale'], key_stats['priceToBook'], key_stats['day200MovingAvg'],
            key_stats['day50MovingAvg'])
        handler_input.response_builder.speak(message)
        return handler_input.response_builder.response

class GetPriceHandler(AbstractRequestHandler):
    # Handler for Price Intent
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("PriceIntent")(handler_input)
        
    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetPriceHandler")
        company = util.get_resolved_value(handler_input.request_envelope.request, "company")
        symbol = util.get_stock_symbol(company)
        price = util.get_stock_price(symbol)
        message = data.PRICE_MESSAGE.format(company, price['price'])
        handler_input.response_builder.speak(message)
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
skill.add_request_handler(HelpIntentHandler())
skill.add_request_handler(CancelorStoporPauseIntentHandler())
skill.add_request_handler(FallbackIntentHandler())
skill.add_request_handler(SessionEndedRequestHandler())
skill.add_request_handler(GetQuoteHandler())
skill.add_request_handler(GetNewsHandler())
skill.add_request_handler(GetKeyStatHandler())
skill.add_request_handler(GetPriceHandler())

# Register exception handler to the skill
skill.add_exception_handler(CatchAllExceptionsHandler())

# Initiate response and request logs
skill.add_global_request_interceptor(RequestLogger())
skill.add_global_response_interceptor(ResponseLogger())

# Register lambda handler in AWS Lambda
lambda_handler = skill.lambda_handler()