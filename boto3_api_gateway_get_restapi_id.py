import boto3_helper
import pprint
import json

session = boto3_helper.init_aws_session()
api_gateway = session.client('apigateway')
pprint.pprint (api_gateway.get_rest_apis())
pprint.pprint (api_gateway.get_deployments(restApiId='41a9v8ivkj'))
export = api_gateway.get_export(restApiId='41a9v8ivkj', stageName='dev', exportType='oas30')['body']
print('URL: ', json.loads(export.read())['servers'])
