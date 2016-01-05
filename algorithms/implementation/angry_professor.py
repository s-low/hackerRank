#!/bin/python

import sys


def handleTest(n, k, arr):
    late = 0
    for i in range(0, n):
        time = arr[i]
        if time > 0:
            late += 1
    ontime = n - late
    if ontime < k:
        print "YES"
    else:
        print "NO"

t = int(raw_input().strip())
for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))

    handleTest(n, k, a)
