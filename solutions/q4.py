#!/bin/python3

import sys

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product(n):
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < n and is_palindrome(product):
                max_palindrome = max(max_palindrome, product)
            if product < max_palindrome:
                break
    return max_palindrome

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_palindrome_product(n))
