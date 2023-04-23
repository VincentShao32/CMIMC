import math
from statistics import mode, median


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
