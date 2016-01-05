#!/bin/python

import sys

summer = False
spring = True
season = True


def getHeight(n):
    global spring
    global summer
    global season

    season = True
    height = 1
    for cycle in xrange(n):
        if season is spring:
            height = height * 2
        elif season is summer:
            height = height + 1

        season = not season

    return height

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print getHeight(n)
