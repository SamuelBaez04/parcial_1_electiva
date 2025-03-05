import json


def hello(event, context):
    body = {
        "message": "Hello world, this is a example of how create a Api with Serverless",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
