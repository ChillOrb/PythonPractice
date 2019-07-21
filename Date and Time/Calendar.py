''' Problem: https://www.hackerrank.com/challenges/calendar-module/problem'''



import calendar


x, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, x, d)].upper())
