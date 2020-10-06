from datetime import datetime, timedelta

import pytz

from util import SessionUtil

session = SessionUtil.get_session()
xray_client = session.client('xray')

start_time = datetime(2020, 10, 5, tzinfo=pytz.timezone('US/Pacific'))
end_time = start_time + timedelta(hours=1)

print(start_time)
print(end_time)

paginator = xray_client.get_paginator('get_trace_summaries')

summaries = paginator.paginate(
    StartTime=start_time,
    EndTime=end_time,
    FilterExpression=''
)

for summary in summaries:
    print(summary)
