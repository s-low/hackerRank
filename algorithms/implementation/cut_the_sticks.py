#!/bin/python

import sys


def cut(sticks):
    new_sticks = []
    cut_by = min(sticks)
    for stick in sticks:
        new = stick - cut_by
        if new > 0:
            new_sticks.append(new)

    return new_sticks

n = int(raw_input().strip())
sticks = map(int, raw_input().strip().split(' '))

length = n
while length != 0:
    print length
    sticks = cut(sticks)
    length = len(sticks)
