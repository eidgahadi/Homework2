#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr = sorted(arr)
print(sum(arr[:-1]), sum(arr[1:]))

