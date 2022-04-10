import boto3
import json

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
  name = event['name']
  location = event['location']
  email_id = event['email_id']
  company_name = event['company_name']
  dynamo_resp = dynamodb.put_item(TableName='UserData', Item={'name':{'S':name},'location':{'S':location},'email_id':{'S':email_id},'company_name':{'S':company_name}})
  print(event)
  
  return {
        'statusCode': 200,
        'body': json.dumps(dynamo_resp)
    }