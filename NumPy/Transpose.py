'''https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem'''

import numpy

n, m = map(int, input().split())

array = numpy.array([input().strip().split() for x in range(n)], int)

print (array.transpose())

print (array.flatten())
