"""
Edit this file! This is the file you will submit.
"""

import random

# Implement me!
# 2 example strategies to use in your tournament.


def f(x):
    return max(0, 1.05 ** (x - 2) - 1)


def lastPlusOneExp(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * min(1, (0.4 + f(len(history)))):
        return 0
    return int(history[-1][0] + 1)


def get_strategies():
    """
    Returns a list of strategy functions to use in a tournament.

    In the local tester, all of the strategies will be used as separate bidders in the tournament.
    Note that strategies are tracked by their function name for readability in the results, so 
    adding the same function multiple times will not simulate multiple bidders using the same strategy.

    In the official grader, only the first element of the list will be used as your strategy. 
    """
    strategies = ([lastPlusOneExp])

    return strategies
