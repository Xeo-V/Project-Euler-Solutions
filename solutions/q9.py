#!/bin/python3

import sys

def find_max_triplet_product(N):
    max_product = -1
    if N % 2 == 0:
        for a in range(1, N // 3):
            b = (N**2 - 2*N*a) / (2*N - 2*a)
            if b.is_integer():
                b = int(b)
                c = N - a - b
                if c > b and a**2 + b**2 == c**2:
                    max_product = max(max_product, a * b * c)
    return max_product

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = find_max_triplet_product(n)
    print(result)
