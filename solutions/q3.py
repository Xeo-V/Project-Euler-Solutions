#!/bin/python3

import sys

def largest_prime_factor(n):
    largest = 2
    while n % 2 == 0:
        n //= 2
    divisor = 3
    while n != 1 and divisor * divisor <= n:
        while n % divisor == 0:
            largest = divisor
            n //= divisor
        divisor += 2
    if n > 2:
        largest = n
    return largest

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
