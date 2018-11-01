import json
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.serialize import DefaultSerializer
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractResponseInterceptor, AbstractRequestInterceptor)
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_core.response_helper import (
    get_plain_text_content, get_rich_text_content)

from ask_sdk_model.interfaces.display import (
    ImageInstance, Image, RenderTemplateDirective, ListTemplate1,
    BackButtonBehavior, ListItem, BodyTemplate2, BodyTemplate1)
from ask_sdk_model import ui, Response

from alexa import data, util


# Skill Builder Object
skill = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Built-In Intent Handlers
class LaunchRequestHandler(AbstractRequestHandler):
    # Handler for Skill Launch
    def can_handle(self, handler_input):
        # type: (HandlerInput) bool
        return is_request_type("LaunchRequest")(handler_input)
    def handle(self, handler_input):
        # type (HandlerInput) Response
        logger.info("In LaunchRequestHandler")
        handler_input.response_builder.speak(data.WELCOME_MESSAGE)
        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    # Handler for Help Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)
    def handle(self, handler_input):
        #type (HandlerInput) Response
        logger.info("In HelpIntentHandler")
        handler_input.attributes_manager.session_attributes = {}
        # Resetting session

        handler_input.response_builder.speak(data.HELP_MESSAGE).ask(data.HELP_PROMPT)
        return handler_input.response_builder.response

class CancelorStoporPauseIntentHandler(AbstractRequestHandler):
    # Handler for Cancel, Pause, or Stop Intents
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or 
                is_intent_name("AMAZON.StopIntent")(handler_input) or
                is_intent_name("AMAZON.PauseIntent")(handler_input))
    def handle(self, handler_input):
        # type (HandlerInput) Response
        logger.info("In CancelorStoporPauseIntentHandler")
        handler_input.response_builder.speak(data.STOP_MESSAGE)
        return handler_input.response_builder.response

class FallbackIntentHandler(AbstractRequestHandler):
    # Handler for Fallback Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type (HandlerInput) response
        logger.info("In FallbackIntentHandler")
        handler_input.response_builder.speak(data.FALLBACK_MESSAGE).ask(data.FALLBACK_PROMPT)
        return handler_input.response_builder.response

class SessionEndedRequestHandler(AbstractRequestHandler):
    # Handler for Session End
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_request_type("SessionEndedRequest")(handler_input)
    def handle(self, handler_input):
        # type (HandlerInput) Response
        logger.info("In SessionEndedRequestHandler")
        logger.info("Session ended reason: {}".format(handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response

class CatchAllExceptionsHandler(AbstractExceptionHandler):
    # Handler for all Exceptions
    def can_handle(self, handler_input, exception):
        # type (HandlerInput, exception) bool
        return True
    def handle(self, handler_input, exception):
        # type (HandlerInput, exception) Response
        logger.info("In CatchAllExceptionsHandler")
        logger.error(exception, exc_info = True)
        handler_input.response_builder.speak(data.EXCEPTION_MESSAGE).ask(data.HELP_PROMPT)
        return handler_input.response_builder.response

# Custom Intent Handlers
class GetQuoteHandler(AbstractRequestHandler):
    # Handler for Quote Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("quote")(handler_input)

class GetNewsHandler(AbstractRequestHandler):
    # Handler for News Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("news")(handler_input)

class GetKeyStatHandler(AbstractRequestHandler):
    # Handler for Key Stats Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("keystats")(handler_input)

class GetPriceHandler(AbstractRequestHandler):
    # Handler for Price Intent
    def can_handle(self, handler_input):
        # type (HandlerInput) bool
        return is_intent_name("price")(handler_input)

# Request Logger
class RequestLogger(AbstractRequestInterceptor):
    # Log Alexa Requests
    def process(self, handler_input):
        # type (HandlerInput) None
        logger.debug("Alexa Request: {}".format(handler_input.request_envelope.request))
# Response Logger
class ResponseLogger(AbstractResponseInterceptor):
    # Log Alexa Responses
    def process(self, handler_input, response):
        # type (HandlerInput) None
        logger.debug("Alexa Response: {}".format(response))