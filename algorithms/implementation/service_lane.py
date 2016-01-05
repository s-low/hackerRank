#!/bin/python

import sys


n, t = raw_input().strip().split(' ')
n, t = [int(n), int(t)]
width = map(int, raw_input().strip().split(' '))
for a0 in xrange(t):
    i, j = raw_input().strip().split(' ')
    i, j = [int(i), int(j)]
    # print "entry:", i
    # print "exit:", j

    # handle each test case
    narrowest = 3
    for e in xrange(i, j + 1):
        # print "width:", width[e]
        if width[e] < narrowest:
            narrowest = width[e]
    print narrowest
