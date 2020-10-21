from flask import Blueprint, Response

APP_BLUEPRINT = Blueprint('app_blueprint', __name__)


@APP_BLUEPRINT.route('/helloWorld', methods=['GET'])
def hello_world():
    return Response('hello world!', status=200)
