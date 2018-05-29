import json
def lambda_handler(event, context):
    body = {
    'AWS lambda' : 'UPDATED 2:57pm'} 
    return {
      'statusCode': 200, 
      'body': json.dumps(body)
      }