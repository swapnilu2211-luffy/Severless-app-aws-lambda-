import json

def handler(event, context):
    # This function processes the incoming web request
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from your 2-Tier Serverless App!')
    }
