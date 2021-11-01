import boto3_helper
import pprint

session = boto3_helper.init_aws_session()
api_gateway = session.client('apigateway')
pprint.pprint (api_gateway.get_resources(restApiId='41a9v8ivkj'))