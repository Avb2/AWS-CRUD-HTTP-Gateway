import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']
    item = json.loads(event['body'])

    update_fields = []
    expression_values = {}
    expression_names = {}

    if 'taskName' in item:
        update_fields.append("taskName = :n")
        expression_values[":n"] = {'S': item['taskName']}

    if 'description' in item:
        update_fields.append("description = :d")
        expression_values[":d"] = {'S': item['description']}

    if 'status' in item:
        update_fields.append("#st = :s")
        expression_values[":s"] = {'S': item['status']}
        expression_names["#st"] = "status"

    if not update_fields:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'No fields to update'})
        }

    update_expression = "SET " + ", ".join(update_fields)

    response = client.update_item(
        TableName='Tasks',
        Key={'TaskId': {'S': task_id}},
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values,
        ExpressionAttributeNames=expression_names,
        ReturnValues="ALL_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response.get("Attributes"))
    }
