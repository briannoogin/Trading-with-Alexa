#Technically this program will take in the json file that was created as a response to the user
#in the lambda function.

#different scenarios to try:
# the table doesn't exist -> create it -> store new item
# the table exists -> load it -> store new item
# the table exits -> load it -> item does not exist -> create new item -> store item

import json
import boto3 #import functionality for dynamodb
import requests

dynamodb = boto3.resource('dynamodb')
#TODO: Find if keyName item exists in the table
def itemExists(tableName,keyName):
    try:
        tableName.get_item(
        Key={
            'StockName': keyName
        }
        )
        return True
    #if it cannot fetch the item (because it doesn't exist)
    except dynamodb.exceptions.DynamoDBKeyNotFoundError:
        return False
    return False

#TODO: create item to then store inside the table
def createItem(table,stockName,time,price,quantity):
    table.put_item(
    Item={
        'StockName': stockName,
        'Time': time,
        'Price': price,
        'quantity': quantity
    }
    )
#creates the StockData table. Only needs to be done once.
def createTable():
    table = dynamodb.create_table(
    TableName='StockData',
    KeySchema=[
        {
            'AttributeName': 'StockName',
            'KeyType': 'HASH'
        },
        {
            #TODO:Figure out how to handle time w/ Python. 
            'AttributeName': 'Time',
            'KeyType': 'NUMBER'
        },
        {
            'AttributeName': 'Price',
            'KeyType': 'NUMBER'
        },
        {
            'AttributeName': 'Quantity',
            'KeyType': 'NUMBER'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Stockname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 15,
        'WriteCapacityUnits': 15
    }
    )
    return table

#
def convertJSON(jsonFile){
    #CALL IEX ON HERE
}

#parameters should include the item we want to update
def updateTable(table):
    #when the table is already created we simply use it
    table = dynamodb.Table('StockData')

def main():
    try:
        #if the table does not exist, create it, then return it
        table=createTable()
        createItem(table,)
    except dynamodb.exceptions.ResourceInUseException:
        #if the table already exists then add item to directly to the table
        print("hi")
