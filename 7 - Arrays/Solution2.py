#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
# This works
#for i in reversed(arr):
#    print i,
arr = arr[::-1]
for i in arr:
    print i,
