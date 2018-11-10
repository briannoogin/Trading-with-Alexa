#different scenarios to try:
# the table doesn't exist -> create it -> store new item
# the table exists -> load it -> store new item
# the table exits -> load it -> item does not exist -> create new item -> store item


import boto3 #import functionality for dynamodb

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
    except dynamodb.exceptions.DynamoDBKeyNotFoundError:
        return False
    return False

#TODO: create item to then store
def createItem(table,stockName,time,price,quantity):
    table.put_item(
    Item={
        'StockName': stockName,
        'Time': time,
        'Price': price,
        'quantity': quantity
    }
    )
)


#TODO: Find out what parameters need to be passed
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


#parameters should include the item we want to update
def updateTable():
    #when the table is already created we simply use it
    table = dynamodb.Table('StockData')


#TODO: Figure out if we need to create a new item or if we need to update values
try:
    createTable()
except dynamodb.exceptions.ResourceInUseException:
    #if the table already exists then update it with the appropriate values
    print("call function")