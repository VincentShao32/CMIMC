"""
Edit this file! This is the file you will submit.
"""
import random
from megamind import megamind
from advay import *
from fiftyFifty import fiftyFifty
from lose import loseOpp
from loseUs import loseUs
from smart import smart
from linear import linear

# Implement me!
# 2 example strategies to use in your tournament.

from statistics import mean, stdev


def f(x):
    return -12 * x + 100
    # return 100 * 0.65 ** x


def standardDev(points):
    if len(points) == 1:
        return points[0]
    return stdev(points)


def roundNum(num):
    return round(num * 100) / 100


def megamath(wallet, history):

    if len(history) == 0:
        return 1

    total = 100
    points1 = [history[0][0] / total]
    total -= history[0][0]
    for i in history[1:]:
        if i[0] < 1:
            continue
        points1.append(roundNum(i[0] / total))
        total -= i[0]
    oppFactor = mean(j for j in points1)
    oppSum = (100 - sum(i[0] for i in history))
    points2 = [history[0][0] / 100]
    for i, j in enumerate(history[1:]):
        if j[0] < 1:
            continue
        points2.append(roundNum(j[0] / f(i - 1)))
    print(points2)
    selfFactor = mean(j for j in points2)
    useFactor = selfFactor if standardDev(
        points2) < standardDev(points1) else oppFactor

    #useFactor = oppFactor
    if useFactor == selfFactor:
        return int(wallet * (useFactor + 0.125))

    if (oppSum * (useFactor + 0.125) > wallet * 0.7):
        return 0
    return int(oppSum * (useFactor + 0.125))

# def ElDesafisimo(wallet, history):
#     if len(history) == 0:
#         return 0

#     if history[-1] == 0 and len(history) < 5:
#         return 1

#     sum_of_wallet = sum(list(map(lambda x: x[0], history)))
#     valid_amount = sum_of_wallet * logistic_function(len(history))

#     return 1 if valid_amount > wallet else valid_amount + 1


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
    strategies = ([megamath, ElDesafisimo, ElDesafio, loseOpp, loseUs, fiftyFifty, smart, loseUs, loseOpp, advay,
                  advay2, ElDesafio, ElDesafisimo, fiftyFifty, randomShit, predatorCounter])
    # strategies = ([gambler] + [megamath])
    # strategies = ([megamath, fiftyFifty])
    return strategies
