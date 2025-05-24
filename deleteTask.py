import json
import boto3
import botocore

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    id = event["pathParameters"]['id']
    try:
        client.delete_item(
            TableName='Tasks',
            Key={
                'TaskId': {
                    'S': id
                }
            }
        )


        return {
            'statusCode': 200,
            'body': json.dumps(f'Task {id} deleted')
        }
    except botocore.exceptions.ClientError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(str(e))
        }
