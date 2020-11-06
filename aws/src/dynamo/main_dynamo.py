import logging

from src.dynamo.DynamoUtil import DynamoUtil
from src.util import SessionUtil

logging.basicConfig(format="'%(asctime)s' %(name)s [%(threadName)s] : %(message)s'", level=logging.INFO)
logging.getLogger('DynamoUtil').setLevel(logging.DEBUG)

session = SessionUtil.get_session()
dynamo_util = DynamoUtil(session)

items = dynamo_util.scan_for_items(TableName='',
                                   IndexName='',
                                   ProjectionExpression='')
