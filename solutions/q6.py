#!/bin/python3

import sys

def difference_of_sums(n):
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2
    return abs(sum_of_squares - square_of_sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(difference_of_sums(n))
