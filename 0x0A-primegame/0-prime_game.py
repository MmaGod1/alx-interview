#!/usr/bin/python3
"""Prime Game. """


def isWinner(x, nums):
    """Find the winner of the game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(max_n**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, max_n + 1, p):
                primes[multiple] = False

    prime_list = [i for i, is_prime in enumerate(primes) if is_prime]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(1 for i in prime_list if i <= n)

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
