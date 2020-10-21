from aws_cdk import aws_apigateway


def create_api_gateway(stack, id, api_lambda):
    api_name = '%s-api' % id
    options = aws_apigateway.StageOptions(logging_level=aws_apigateway.MethodLoggingLevel.INFO, data_trace_enabled=True)
    return aws_apigateway.LambdaRestApi(stack, api_name,
                                        rest_api_name=api_name,
                                        deploy_options=options,
                                        handler=api_lambda)