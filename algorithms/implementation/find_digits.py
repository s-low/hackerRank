#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    count = 0
    n_str = str(n)
    for ch in n_str:
        digit = int(ch)
        if digit != 0 and n % digit == 0:
            count += 1
    print count
