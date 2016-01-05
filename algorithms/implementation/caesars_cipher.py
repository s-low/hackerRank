#!/bin/python

import sys

Z = 90
z = 122
a = 97
ALPHABET = 26

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

s = list(s)
for idx, ch in enumerate(s):
    # if character is a letter
    if ch.isalpha():
        # shift through the alphabet
        original = ord(ch)
        replacement = original + k % 26

        # loop round the end of alphabet (z->a and Z->A)
        if replacement > Z and original >= a:
            replacement = replacement - ALPHABET
        elif replacement > Z and original <= Z:
            replacement = replacement - ALPHABET
        ch = chr(replacement)
        s[idx] = ch

print ''.join(s)
