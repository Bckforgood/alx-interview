#!/usr/bin/python3
"""Prime Game implementation."""


def isWinner(x, nums):
    """
    Determine the winner of each game played x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the range for each round.

    Returns:
        str or None: Name of the player that won the most rounds.
        None if the winner cannot be determined.
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_score = 0
    maria_score = 0

    prime_flags = [1 for x in range(sorted(nums)[-1] + 1)]
    prime_flags[0], prime_flags[1] = 0, 0
    for i in range(2, len(prime_flags)):
        remove_multiples(prime_flags, i)
    for i in nums:
        if sum(prime_flags[0:i + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score > maria_score:
        return "Ben"
    if maria_score > ben_score:
        return "Maria"
    return None


def remove_multiples(list_primes, prime):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.
    """
    for i in range(2, len(list_primes)):
        try:
            list_primes[i * prime] = 0
        except (ValueError, IndexError):
            break
            break
