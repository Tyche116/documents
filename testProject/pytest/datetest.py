import datetime
from dateutil.relativedelta import relativedelta
 
datetime_now = datetime.datetime.now()
print(datetime_now.year)
print(datetime_now.month)
print(datetime_now.day)
print(datetime_now.hour)
print(datetime_now.minute)
print(datetime_now.second)
print(datetime_now.microsecond)

datetime_three_month_ago = datetime_now - relativedelta(months=8)

print(datetime_three_month_ago)

print("==> ", int(datetime_three_month_ago.timestamp()))