import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    response = json.dumps(
            client.get_item(
                TableName='Tasks',
                Key={
                    'TaskId': {
                        'S': event['pathParameters']['id']
                    }
                }
                ).get('Item')
        )
    if response:
        return {
            'statusCode': 200,
            'body': response
        }
    else: 
        return {
            'statusCode': 404,
            'body': 'Task not found'
        }
    
