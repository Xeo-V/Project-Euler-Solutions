from math import factorial

for _ in range(int(input())):
    items = input().split()
    n = int(items[0])
    m = int(items[1])
    result = factorial(n + m) // factorial(n) // factorial(m)
    print(result % (10**9 + 7))
