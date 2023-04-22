"""
Edit this file! This is the file you will submit.
"""
import random
from megamath import megamath
from advay import *
from fiftyFifty import fiftyFifty
from lose import loseOpp
from loseUs import loseUs
from smart import smart
from linear import linear
from constant import constant
from variation import variation
from megamathCounter import randomShit
from megamind import megamind
from lastPlusOne import lastPlusOne

# Implement me!
# 2 example strategies to use in your tournament.

from statistics import stdev, median, mode
import math


def f(x):
    return -12 * x + 100


def standardDev(points):
    if len(points) == 1:
        return points[0]
    return stdev(points)


def roundNum(num):
    return round(num * 100) / 100


def constantValue(history):
    vals = [i[0] for i in history]
    mid = median(vals)
    if mid == mode(vals):
        return True, mid
    return False, -1


def megamath(wallet, history):
    oppSum = (100 - sum(i[0] for i in history))
    if len(history) == 0:
        return 0

    constant, val = constantValue(history)
    if constant and val + 1 < wallet * 0.5:
        return val + 1

    total = 100
    points1 = [history[0][0] / total]
    total -= history[0][0]
    for i in history[1:]:
        if i[0] < 2:
            continue
        points1.append(roundNum(i[0] / total))
        total -= i[0]
    oppFactor = median(j for j in points1)

    points2 = [history[0][0] / 100]
    for i, j in enumerate(history[1:]):
        if j[0] < 2:
            continue
        points2.append(roundNum(j[0] / f(i - 1)))
    selfFactor = median(j for j in points2)
    useFactor = selfFactor if standardDev(
        points2) < standardDev(points1) else oppFactor

    # useFactor = oppFactor
    if useFactor == selfFactor:
        return min(wallet, int(wallet * (useFactor + 0.125)))

    if (oppSum * (useFactor + 0.125) > wallet * 0.5):
        return 0
    return int(oppSum * (useFactor + 0.125))


def mCalc(n, points):
    prodSum = 0
    xSum = 0
    ySum = 0
    xSquaredSum = 0
    for x, point in enumerate(points):
        prodSum += x * point
        xSum += x
        ySum += point
        xSquaredSum += x ** 2

    return roundNum((n * prodSum - xSum * ySum) / (n * xSquaredSum - xSum ** 2)), xSum, ySum


def bCalc(m, n, xSum, ySum):
    return roundNum((ySum - m * xSum) / n)


def linRegression(points):
    m, xSum, ySum = mCalc(len(points), points)
    b = bCalc(m, len(points), xSum, ySum)
    return m, b


def roundNum(num):
    return round(num * 100) / 100


def g(m, b, x):
    return m * x + b


def RMSE(m, b, points):
    errSum = 0
    for i, point in enumerate(points):
        errSum += (point - g(m, b, i)) ** 2
    return math.sqrt((1 / len(points)) * errSum)


def constantValue(history):
    vals = [i[0] for i in history]
    mid = median(vals)
    if mid == mode(vals):
        return True, mid
    return False, -1


def megamind(wallet, history):
    oppSum = (100 - sum(i[0] for i in history))
    if len(history) == 0:
        return 2
    constant, val = constantValue(history)
    if constant and val + 1 < wallet * 0.6:
        return int(val + 1)
    oppBets = [history[0][0] / 100]
    total = 100 - history[0][0]
    for i in history[1:]:
        if i[0] < 2:
            continue
        oppBets.append(roundNum(i[0] / total))
        total -= i[0]
    if len(oppBets) >= 2:
        oppm, oppb = linRegression(oppBets)

        oppNext = g(oppm, oppb, len(oppBets))
    else:
        oppNext = 0.2

    # selfBets = [history[0][0] / 100]
    # for i, j in enumerate(history[1:]):
    #     if j[0] < 1:
    #         continue
    #     selfBets.append(roundNum(j[0] / f(i - 1)))

    # if len(selfBets) >= 2:
    #     selfm, selfb = linRegression(selfBets)
    #     # for i in history:
    #     #     print(i[0])
    #     selfNext = g(selfm, selfb, len(selfBets))
    # else:
    #     selfNext = 0.2

    # if selfNext == oppNext:
    #     return int(oppSum * selfNext)
    # use = oppNext if RMSE(oppm, oppb, oppBets) < RMSE(
    #     selfm, selfb, selfBets) else selfNext

    if oppSum * oppNext > wallet * 0.6:
        return 0

    return int(wallet * oppNext)


def lastPlusOne(wallet, history):
    # roundFactor = 0.00 * len(history)
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * 0.5:
        return 0

    return int(history[-1][0] + 1)


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
    strategies = ([lastPlusOne] + [linear] * 10)
    # strategies = ([gambler] + [megamath])
    # strategies = ([megamath, fiftyFifty])
    return strategies
