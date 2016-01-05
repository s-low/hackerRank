#!/bin/python

import sys
import math

t = int(raw_input().strip())
for a0 in xrange(t):
    n, c, m = raw_input().strip().split(' ')
    n, c, m = [int(n), int(c), int(m)]

    # how many chocolates (and wrappers) can bob buy
    chocs = wrappers = n / c

    # while he has enough wrappers in hand to exchange
    while wrappers >= m:
        gets_free = wrappers / m

        # update totals
        wrappers = wrappers % m
        wrappers = wrappers + gets_free
        chocs += gets_free

    print chocs
