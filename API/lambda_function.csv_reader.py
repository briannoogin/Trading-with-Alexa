import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def csv_reader(event, context):
   
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']
   
   obj = s3.get_object(Bucket = bucket, Key = key)
   
   rows = obj['Body'].read().split('\n')
   
   table = dynamodb.Table('company_data')
   
   with table.batch_writer() as batch:
       for row in rows:
           batch.put_item(Item = {
               
               'Symbol':row.split(',')[0],
               'Name' :row.split(',')[1] ,
               "LastScale" :row.split(',')[2] ,
               'MarketCap' :row.split(',')[3] ,
               'ADR TSO' :row.split(',')[4],
               'Sector' :row.split(',')[5],
               'Industry' :row.split(',')[6],
               'Summary Quote' :row.split(',')[7],
               
           })
