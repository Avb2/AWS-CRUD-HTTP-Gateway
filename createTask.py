import boto3
import uuid
import botocore
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    uid = str(uuid.uuid4())
    try:
        client.put_item(
            TableName='Tasks',
            Item={
                'TaskId': {'S': uid},
                'taskName': {'S': body['taskName']},
                'description': {'S': body['description']},
                'status': {'S': body['status']}
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f'Task created. TaskId: {uid}')
        }
    except botocore.exceptions.ClientError as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error creating task')
        }
