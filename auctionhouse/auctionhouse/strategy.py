"""
Edit this file! This is the file you will submit.
"""
import random
from lose import loseOpp
from advay import *
from loseUs import loseUs
from fiftyFifty import fiftyFifty
from smart import smart
from advay import *
from predatorCounter import predatorCounter
from average import average
from megamath import megamath, megamathv2

# Implement me!
# 2 example strategies to use in your tournament.


def gambler(wallet, history):
    return random.randint(0, wallet)


def villain(wallet, history):
    return max(wallet - 1, 0)

# Edit me!


def get_strategies():
    """
    Returns a list of strategy functions to use in a tournament.

    In the local tester, all of the strategies will be used as separate bidders in the tournament.
    Note that strategies are tracked by their function name for readability in the results, so 
    adding the same function multiple times will not simulate multiple bidders using the same strategy.

    In the official grader, only the first element of the list will be used as your strategy. 
    """
    strategies = ([loseUs, loseOpp, fiftyFifty, advay2, smart,
                  average, ElDesafio, ElDesafisimo, megamath])
    # strategies = ([gambler] + [megamath])
    # strategies = ([megamath, fiftyFifty])
    return strategies
