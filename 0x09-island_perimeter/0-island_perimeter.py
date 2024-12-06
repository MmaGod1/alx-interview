#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Calculates an island primeter. """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] != 1:
                    perimeter += 1
                if i == 0 or grid[i - 1][j] != 1:
                    perimeter += 1
                if j + 1 == len(grid[0]) or grid[i][j + 1] != 1:
                    perimeter += 1
                if i + 1 == len(grid) or grid[i + 1][j] != 1:
                    perimeter += 1
    return perimeter
