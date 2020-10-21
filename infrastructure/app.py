#!/usr/bin/env python3
from aws_cdk import core
from cdk.cdk_stack import InfrastructureStack


app = core.App()

InfrastructureStack(app, 'dev-aws-cdk-api-lambda-flask', env=core.Environment(account='', region='us-east-1'))
InfrastructureStack(app, 'prod-aws-cdk-api-lambda-flask', env=core.Environment(account='', region='us-east-1'))

app.synth()
