import math


def lin(m, b, x):
    return max(0, roundNum(m * x + b))


def roundNum(num):
    return round(num * 1000) / 1000


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


def average(data):
    return roundNum(sum(data) / len(data))


def isConstant(lst):
    constant = True
    for i, j in enumerate(lst):
        if j != lst[i - 1]:
            constant = False
            break
    return constant


def RMSE(m, b, points):
    errSum = 0
    for i, point in enumerate(points):
        errSum += (point - lin(m, b, i)) ** 2
    return math.sqrt((1 / len(points)) * errSum)


def smarter(wallet, history):
    if len(history) == 0:
        return 0

    oppSum = (100 - sum(i[0] for i in history))

    increase = False

    oppBets = []
    for i in history:
        if i[0] < 2:
            continue
        oppBets.append(i[0])

    if len(oppBets) >= 2 and not isConstant(oppBets):
        slope, intercept = linRegression(oppBets)
        oppNext = min(oppSum, lin(slope, intercept, len(oppBets) + 1) + 4)

        if RMSE(slope, intercept, oppBets) < 4:
            increase = True

    use = oppNext if increase else history[-1][0] + 1

    if use > wallet * min(1, (0.4 + g(len(history)))):
        return 0

    return int(use)
