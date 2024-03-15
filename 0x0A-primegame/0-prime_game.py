#!/usr/bin/python3
"""Prime Game """


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(n):
    """Generate all prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    # Generate all primes up to the maximum value in nums
    max_num = max(nums)
    primes = generate_primes(max_num)

    # Simulate the game for each round
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for prime in primes if prime <= n)
        # If the count is odd, Maria wins; otherwise, Ben wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner based on the number of wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
