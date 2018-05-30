import json
def lambda_handler(event, context):
    body = {
    'AWS lambda' : 'UPDATED 6:15pm'} 
    return {
      'statusCode': 200, 
      'body': json.dumps(body)
      }