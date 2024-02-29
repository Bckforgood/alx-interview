#!/usr/bin/python3
"""
Module for the makeChange function to determine the fewest
number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest
    number of coins needed to meet a given amount total.

    Args:
        coins: list of coin denominations
        total: total amount to make with coins

    Returns:
        Fewest number of coins needed to meet total
            - If total is 0 or less, return 0
            - If total cannot be met by any number of coins you have, return -1
    """

    if total < 0:
        return 0

    dp = [0] + [float('inf')] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
