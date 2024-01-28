import math

limt = 10**6
sieve_array = [True]*(limt+1)
sieve_array[0] = sieve_array[1] = False

for index in range(2, int(math.sqrt(limt)+1)):
    if sieve_array[index]:
        for multiple in range(index*index, limt+1, index):
            sieve_array[multiple] = False

cumulative_sums = [0]
current_sum = 0
for i in range(1, limt+1):
    if sieve_array[i]:
        current_sum += i
    cumulative_sums.append(current_sum)

t = int(input().strip())
for _ in range(t):
    num = int(input().strip())
    print(cumulative_sums[num])
