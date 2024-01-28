import sys

def sum_of_multiples(limit):
    def sum_multiples(n):
       
        p = (limit - 1) // n
        
        return n * p * (p + 1) // 2
    return sum_multiples(3) + sum_multiples(5) - sum_multiples(15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_of_multiples(n))
