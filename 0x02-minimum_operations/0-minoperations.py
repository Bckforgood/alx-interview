#!/usr/bin/python3
"""
Method that calculates the fewest number of
operations needed to result in exactly n H characters.
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))
                break

    return operations[n] if operations[n] != float('inf') else 0
