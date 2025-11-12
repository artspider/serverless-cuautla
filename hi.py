import json


def hi(event, context):
    body = {
        "message": "Hola Tecnologico de Cuautla!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
