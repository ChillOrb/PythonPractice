 '''Problem: https://www.hackerrank.com/challenges/python-time-delta/problem'''



from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'

for x in range(int(input())):
    time1 = dt.strptime(input(), fmt)
    time2 = dt.strptime(input(), fmt)
    print(int(abs((time1 - time2).total_seconds())))
