from datetime import datetime, timedelta

import pytz

from src.util import SessionUtil

session = SessionUtil.get_session()
xray_client = session.client('xray')


def print_summaries(start_time, end_time, filter_expression=''):
    paginator = xray_client.get_paginator('get_trace_summaries')
    summaries = paginator.paginate(
        StartTime=start_time,
        EndTime=end_time,
        FilterExpression=filter_expression
    )
    for summary in summaries:
        print(summary)


start_time = datetime(2020, 10, 5, tzinfo=pytz.timezone('US/Pacific'))
end_time = start_time + timedelta(hours=1)

print_summaries(start_time, end_time)
