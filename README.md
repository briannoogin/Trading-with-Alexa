# Trading-with-Alexa

Team members will use Alexa SDK and TradeStation API to trade on the stock market with Amazon Alexa.

## Table of Contents
   
 * [Introduction](#introduction)
 * [Built With](#built-with)
 * [Dependencies](#dependencies)
 * [Installation](#installation)
 * [License](#license)
 * [Attribution](#attribution)
 * [Authors](#authors)


### Introduction
------------

 There is a lack of user-friendly tools to retrieve stock information real-time and websites often become too complex to navigate. The Trading with Alexa Skill is a user friendly application that gives real-time stock information and allows users to make more informed investment decisions and at the very least, educate users on the state of the stock market.

### Built With
------------

 * [Alexa Skills Kit](https://developer.amazon.com/alexa-skills-kit "Alexa Skill Kit Homepage") - The Skills Kit
 * [IEX Trading API](https://iextrading.com/developer/docs/ "IEX API Documentation") - Used to retrieve stock data
 * [Yahoo Finance API](https://finance.yahoo.com/ "Yahoo Finance Homepage") - Used to convert company name to respective stock ticker symbol

### Dependencies
----------------

Please see the [requirements.txt](requirements.txt) file for all dependencies
You will also need:
   * An Amazon Echo or other Alexa-enabled device
   * An AWS account (AWS Lambda, Alexa-skill configuration, optional Cloudwatch logging)

### Installation
----------------
* Create a Python virtual environment, and install the contents of the requirements.txt file into it using `pip`
* Zip the contents of the `site-packages` folder within your virtual environment (remember, zip the contents of the director, not the directory itself)
* Add the contents of lambda/py to the zip file also (alexa/.. and lambda_function.py)
* Once this zip is ready, create your Lambda function using AWS Lambda (a quick google search should return some useful guides, [see this guide](https://github.com/alexa/skill-sample-python-city-guide/blob/master/instructions/2-lambda-function.md))
* Create your Alexa skill, and when editing intents, you can use "manual edit", and paste in the contents of the models/skill.json file
* Take the skill ID of the Alexa skill, and add "Alexa Skills Kit" as a trigger in your Lambda function. Enable Skill ID verification, and paste in your skill ID.
* Under `Endpoints` in the Alexa skill, paste the ARN of your Lambda function.

You should be good to test it at this point! We recommend using the built-in `Test` console on the Alexa skill before you load it on your own Alexa. 

### License
-----------

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

### Attribution
---------------

 * Data provided for free by IEX. View IEX’s [Terms of Use](https://iextrading.com/api-exhibit-a/ "IEX Terms of Use").
 * Company to symbol conversion provided for free by [Yahoo Finance](https://finance.yahoo.com/ "Yahoo Finance Homepage").
 <a href="https://finance.yahoo.com/" target="_blank"> <img src="https://poweredby.yahoo.com/purple.png" width="134" height="29"/> </a>

### Authors
-----------

 * Madhav Mehta
 * Sabal Ranabhat
 * Cameron O'Brien
 * Karina Scott
 * Yohan Flores
 * Brian Nguyen
