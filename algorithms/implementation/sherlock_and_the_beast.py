#!/bin/python

import sys


def decent_number(digits):
    if digits < 3:
        return -1

    # create some strings
    three = str(3)
    five = str(5)

    # if the number of digits is divisible by 3 use 555-555-555
    if not digits % 3:
        return five * digits
    # if the number of digits is exactly 5 use 33333
    elif digits == 5:
        return three * digits

    # find the digits/3 remainder
    for num in xrange(digits / 3, -1, -1):
        diff = digits - 3 * num

        # if the remainder is divisible by 5
        if not diff % 5:
            # tack on 33333-33333...
            return five * 3 * num + three * diff

    # otherwise fail
    return -1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print decent_number(n)
