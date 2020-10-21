import os

from aws_cdk import aws_lambda


def create_flask_lambda(stack, id):
    lambda_name = '%s-lambda' % id
    lambda_files = os.path.join(os.path.dirname(__file__), '..', '..', 'application')
    return aws_lambda.Function(stack, lambda_name,
                               runtime=aws_lambda.Runtime.PYTHON_3_7,
                               handler='lambda_app.handler',
                               function_name=lambda_name,
                               code=aws_lambda.Code.from_asset(lambda_files),
                               environment={'SAMPLE_ENV_VAR': 'fake env var'})
