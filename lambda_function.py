import json
def lambda_handler(event, context):
    body = {
    'AWS lambda' : 'UPDATED'} 
    return {
      'statusCode': 200, 
      'body': json.dumps(body)
      }