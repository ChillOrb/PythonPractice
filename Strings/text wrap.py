'''Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
'''
import textwrap
s = input()
w = int(input().strip())
print(textwrap.fill(s,w))
