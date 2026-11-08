import json

def lambda_handler(event, context):

    message = {
        "message": "Welcome to Serverless Task API!",
        "status": "success",
        "project": "AWS Lambda and API Gateway",
        "developer": "Nahdiya"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(message)
    }
