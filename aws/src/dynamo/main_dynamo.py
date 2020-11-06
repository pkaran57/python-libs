from src.util import SessionUtil

session = SessionUtil.get_session()
dynamo_client = session.client('dynamodb')


def describe_table(table_name):
    description = dynamo_client.describe_table(TableName=table_name)

    for key, value in description['Table'].items():
        print('\n{}:\n{}'.format(key, value))


describe_table('table_name')
