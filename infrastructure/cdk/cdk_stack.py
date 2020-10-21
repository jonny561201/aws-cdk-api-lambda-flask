from aws_cdk import core
from cdk.lambdas import create_flask_lambda
from cdk.api_gateway import create_api_gateway


class InfrastructureStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        flask_lambda = create_flask_lambda(self, id)
        api = create_api_gateway(self, id, flask_lambda)
