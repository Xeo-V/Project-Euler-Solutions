def calculate_partial_sum(size, multiplier):
    half_size = (size + 1) // 2
    return size * (size + 1) * (size + 2) // 6 - multiplier * half_size * (1 + size) // 2 + multiplier * half_size

def calculate_diagonal_sum(size):
    total_sum = sum(calculate_partial_sum(size, i) for i in range(4)) - 3
    return total_sum % (10**9 + 7)

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        grid_size = int(input())
        print(calculate_diagonal_sum(grid_size))
