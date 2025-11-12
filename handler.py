import json


def hello(event, context):
    body = {
        "message": "Hola Tecnológico de Cuautla!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
