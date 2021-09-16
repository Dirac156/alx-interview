#!/usr/bin/python3
""" perimiter of an island """


def island_perimeter(grid):
    """
    Find perimeter of the island
    """
    count = 0
    rows = len(grid)
    columns = 0
    if (rows):
        col = len(grid[0])
    

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            idx = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            check = [1 if k[0] in range(rows) and k[1] in range(columns) else 0
                     for k in idx]

            if grid[i][j]:
                count += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idx)])

    return (count)
