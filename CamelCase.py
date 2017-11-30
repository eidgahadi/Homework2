#!/bin/python3

import sys

s = input().strip()
res = 1
for c in s:
    if c.isupper():
        res += 1

print(res)