#!/bin/python3

import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple(n):
    ans = 1
    for i in range(1, n + 1):
        ans = lcm(ans, i)
    return ans

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))
