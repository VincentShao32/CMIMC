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
