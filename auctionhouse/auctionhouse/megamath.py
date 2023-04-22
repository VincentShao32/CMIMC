from statistics import mean, stdev


def f(x):
    return -12 * x + 100
    # return 100 * 0.65 ** x


def standardDev(points):
    if len(points) == 1:
        return points[0]
    return stdev(points)


def megamath(wallet, history):
    if len(history) == 0:
        return 1

    subtract = 0
    points1 = [history[0][0] / 100]
    subtract += history[0][0]
    for i in history[1:]:
        if i[0] < 3:
            continue
        points1.append(i[0] / (100 - subtract + 0.05))
        subtract += i[0]
    oppFactor = mean(j for j in points1)
    oppSum = (100 - sum(i[0] for i in history))
    points2 = [history[0][0] / 100]
    for i, j in enumerate(history[1:]):
        if j[0] < 3:
            continue
        points2.append(j[0] / f(i - 1))
    selfFactor = mean(j for j in points2)
    useFactor = selfFactor if standardDev(
        points2) < standardDev(points1) else oppFactor

    # useFactor = oppFactor
    if useFactor == selfFactor:
        return int(wallet * (useFactor + 0.125))

    if (oppSum * (useFactor + 0.125) > wallet * 0.7):
        return 0
    return int(oppSum * (useFactor + 0.125))


def calcSlope(y2, y1):
    return y2 - y1


def roundNum(num):
    return round(num * 1000) / 1000


def megamathv2(wallet, history):
    if len(history) == 0:
        return 1

    subtract = 0
    points1 = []
    if len(history) < 4:
        hist = history
    else:
        hist = history[-3:]

    for i in history[:-3]:
        subtract += i[0]
    for i in hist:
        points1.append(roundNum(i[0] / (100 - subtract + 0.05)))
        subtract += i[0]
    # print(points1)

    if len(points1) == 1:
        slope = 0
    else:
        slope = mean(calcSlope(j, points1[i - 1])
                     for i, j in enumerate(points1[1:]))

    oppFactor = mean(j for j in points1) + slope
    oppSum = (100 - sum(i[0] for i in history))

    points2 = []
    for i, j in enumerate(hist):
        points2.append(roundNum(j[0] / f(i - 1)))
    slope = mean(calcSlope(j, points2[i - 1]) for i, j in enumerate(points2))
    selfFactor = mean(j for j in points2) + slope

    useFactor = selfFactor if standardDev(
        points2) < standardDev(points1) else oppFactor

    if (oppSum * useFactor + 2 > wallet):
        return 0
    return int(oppSum * (useFactor + 0.1))
