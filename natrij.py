from sys import stdin
import time
from datetime import timedelta

#ran this one colab since windows C doesnt support mktime

time1 = input().replace('\n', "")
time2 = input().replace('\n', "")

time1 = time.mktime(time.strptime(time1, '%H:%M:%S'))
time2 = time.mktime(time.strptime(time2, '%H:%M:%S'))

if time1 == time2:
    print("24:00:00")
else:
    timesub = time2-time1
    timesub = time.strftime('%H:%M:%S', time.gmtime(timesub))
    print(timesub)