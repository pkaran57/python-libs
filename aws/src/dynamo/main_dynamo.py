from src.util import SessionUtil

table_name = ''
session = SessionUtil.get_session()

dynamo_client = session.client('dynamodb')
dynamodb_resource = session.resource('dynamodb')
table = dynamodb_resource.Table(table_name)


def describe_table(table_name: str) -> None:
    description = dynamo_client.describe_table(TableName=table_name)

    for key, value in description['Table'].items():
        print('\n{}:\n{}'.format(key, value))


describe_table(table_name)
