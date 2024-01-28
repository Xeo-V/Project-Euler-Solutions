def calculate_sum_of_divisors(max_size):
    sum_divisors = [1] * (max_size + 1)
    sum_divisors[0] = 0
    sum_divisors[1] = 0
    for number in range(2, max_size):
        for multiple in range(2 * number, max_size, number):
            sum_divisors[multiple] += number
    return sum_divisors

def calculate_sum_of_amicable(max_size, sum_divisors):
    sum_amicable = [0] * max_size
    current_sum = 0
    for number in range(1, max_size):
        a = sum_divisors[number]
        if a < len(sum_divisors) and a != number:
            if sum_divisors[a] == number:
                current_sum += number
        sum_amicable[number] = current_sum
    return sum_amicable

def main():
    max_size = 10 ** 5 + 1
    sum_of_divisors = calculate_sum_of_divisors(max_size)
    sum_of_amicable = calculate_sum_of_amicable(max_size, sum_of_divisors)
    
    num_cases = int(input())
    for case in range(num_cases):
        n = int(input())
        print(sum_of_amicable[n - 1])

if __name__ == "__main__":
    main()
