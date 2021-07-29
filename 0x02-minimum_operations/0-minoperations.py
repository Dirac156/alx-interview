#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n):
    """
    execute the minimum posiible
    """
    if n <= 1:
        return 0

    variable1 = n
    variable2 = 2
    variable3 = 0

    for i in range(2, variable1):
        if variable1 % variable2 == 0:
            variable1 = variable1 / variable2
            variable3 = variable3 + variable2
        else:
            variable2 = variable2 + 1

    return variable3
