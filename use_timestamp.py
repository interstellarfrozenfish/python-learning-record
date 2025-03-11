import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    match = re.match(r'UTC([+-])(\d+):(\d+)', tz_str)
    if match is None:
        raise ValueError('Invalid timezone string')
    
    sign, hours, minutes = match.groups()
    offset = int(hours) * 60 + int(minutes)

    if sign == '-':
        offset = -offset

    tz = timezone(timedelta(minutes=offset))
                  
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = dt.replace(tzinfo=tz)

    return dt.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')