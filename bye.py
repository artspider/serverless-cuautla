import json


def bye(event, context):
    body = {
        "message": "Adios Tecnológico de Cuautla!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
