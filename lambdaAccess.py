import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def csv_reader(event, context):
   
   print(event)
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']
   
   obj = s3.get_object(Bucket = bucket, Key = key)
   
   rows = obj['Body'].read().decode('utf-8').split('\n')
   table = dynamodb.Table('companyNames')
   
   with table.batch_writer() as batch:
      for row in rows:
         batch.put_item(Item = {
            'Symbol':row.split(',')[0],
            'Name' :row.split(',')[1],
            #'Summary Quote' :row.split(',')[7],
         })

