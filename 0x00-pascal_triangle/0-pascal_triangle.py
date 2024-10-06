#!/usr/bin/python3
"""
Module for generating Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing the triangle.
               Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
