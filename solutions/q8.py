#!/bin/python3

import sys

def greatest_product(n, k, number):
    max_product = 0
    for i in range(n - k + 1):
        product = 1
        for j in range(k):
            product *= int(number[i + j])
        max_product = max(max_product, product)
    return max_product

t = int(input().strip())
for a0 in range(t):
    n, k = map(int, input().strip().split())
    number = input().strip()
    print(greatest_product(n, k, number))
