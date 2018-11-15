import boto3
from boto3.dynamodb.conditions import Key
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('companyNames')
    Name = event["key2"]
    response = table.query(
        IndexName='Name-index',
        KeyConditionExpression=Key('Name').eq(Name)
    )
    
    print(response['Items'][0]['Symbol'])
