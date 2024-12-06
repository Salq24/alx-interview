#!/usr/bin/python3
"""
perimeter of island
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    :param grid: List of list of integers representing the map.
    :return: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Start with 4 sides of a single cell
                perimeter += 4

                # Check top neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
