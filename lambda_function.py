import json
def lambda_handler(event, context):
    body = {
    'AWS lambda' : 'UPDATED 4:10pm'} 
    return {
      'statusCode': 200, 
      'body': json.dumps(body)
      }