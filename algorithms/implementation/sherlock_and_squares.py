#!/bin/python

import sys
import math

t = input()
for _ in xrange(t):
    count = 0
    thing = raw_input().strip()
    a = int(thing.split()[0])
    b = int(thing.split()[1])

    # because a < b, rt(a) < rt(b) and all square numbers
    # between a and b will correspond to each integer between
    # rt(a) and rt(b).

    rt_a = math.ceil(math.sqrt(a))
    rt_b = math.floor(math.sqrt(b))
    diff = rt_b - rt_a + 1

    print int(diff)
