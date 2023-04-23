"""
Edit this file! This is the file you will submit.
"""

import random
# from linear import linear
# from smart import smart
# from predatorCounter import predatorCounter
# from megamath import megamath
# from advay import *
# from fiftyFifty import fiftyFifty
# from lose import loseOpp
# from loseUs import loseUs
# from smart import smart
# from linear import linear
# from constant import constant
# from variation import variation
# from megamathCounter import randomShit
# from megamind import megamind
# from lastPlusOne import lastPlusOne, lastPlusOneVaried
# from lastOne import lastOne
# from lastPlusMultiple import *
# from bigSmall import bigSmall
# from average import average, med

# Implement me!
# 2 example strategies to use in your tournament.


def f(x):
    return max(0, 0.08 * (x - 3))


def g(x):
    return max(0, 1.05 ** (x - 2) - 1)


def lastPlusMultiple(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * min(1, (0.3 + f(len(history)))):
        return 0
    return int(history[-1][0] + 1)


def lastPlusMultipleExp(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * min(1, (0.4 + g(len(history)))):
        return 0
    return int(history[-1][0] + 1)


def lastPlusOne(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * 0.5:
        return 0

    return int(history[-1][0] + 1)


# def gambler(wallet, history):
#     return random.randint(0, wallet)


# def refinedGambler(wallet, history):
#     return int(random.uniform(0.1, 0.5) * wallet)


# def villain(wallet, history):
#     return max(wallet - 1, 0)


def get_strategies():
    """
    Returns a list of strategy functions to use in a tournament.

    In the local tester, all of the strategies will be used as separate bidders in the tournament.
    Note that strategies are tracked by their function name for readability in the results, so 
    adding the same function multiple times will not simulate multiple bidders using the same strategy.

    In the official grader, only the first element of the list will be used as your strategy. 
    """
    strategies = ([lastPlusMultipleExp])

    return strategies
