#!/usr/bin/python3
"""Defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle with size n.

    Returns a list of lists of integers representing  triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tria = triangles[-1]
        temp = [1]
        for x in range(len(tria) - 1):
            temp.append(tria[x] + tria[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
