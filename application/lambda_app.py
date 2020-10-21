import awsgi

from src.manager import create_app


def handler(event, context):
    lambda_app = create_app(__name__)
    return awsgi.response(lambda_app, event, context)
