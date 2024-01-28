#!/bin/python3

import sys

def greatest_product(grid):
    max_product = 0
    
    def product_of_four(numbers):
        prod = 1
        for number in numbers:
            prod *= number
        return prod

    for i in range(20):
        for j in range(17): 
            horizontal_prod = product_of_four(grid[i][j:j+4])
            max_product = max(max_product, horizontal_prod)
            vertical_prod = product_of_four([grid[j+k][i] for k in range(4)])
            max_product = max(max_product, vertical_prod)


    for i in range(17):
        for j in range(17):
            diagonal_down_right_prod = product_of_four([grid[i+k][j+k] for k in range(4)])
            max_product = max(max_product, diagonal_down_right_prod)
            diagonal_down_left_prod = product_of_four([grid[i+k][j+3-k] for k in range(4)])
            max_product = max(max_product, diagonal_down_left_prod)

    return max_product

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

print(greatest_product(grid))
