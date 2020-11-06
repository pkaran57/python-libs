import logging


class DynamoUtil:
    _logger = logging.getLogger('DynamoUtil')

    def __init__(self, session):
        self._dynamo_client = session.client('dynamodb')
        self._dynamodb_resource = session.resource('dynamodb')
        # Get Table resource:
        # table = dynamodb_resource.Table(table_name)

    def scan_for_items(self, **kwargs):
        """
        :param kwargs: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html
        """
        scan_paginator = self._dynamo_client.get_paginator('scan')
        response_iterator = scan_paginator.paginate(**kwargs)
        items = []
        for count, response in enumerate(response_iterator):
            items_in_response = response['Items']
            self._logger.debug('Found {} items on {}th iteration of the scan'.format(len(items_in_response), count))
            items.extend(items_in_response)
        return items

    def query_for_items(self, **kwargs):
        """
        :param kwargs: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html
        """
        query_paginator = self._dynamo_client.get_paginator('query')
        response_iterator = query_paginator.paginate(**kwargs)
        items = []
        for count, response in enumerate(response_iterator):
            items_in_response = response['Items']
            self._logger.debug('Found {} items on {}th iteration of the query'.format(len(items_in_response), count))
            items.extend(items_in_response)
        return items

    def describe_table(self, table_name: str) -> None:
        description = self._dynamo_client.describe_table(TableName=table_name)
        for key, value in description['Table'].items():
            print('\n{}:\n{}'.format(key, value))
