from statistics import mean, stdev

def calcSlope(y2, y1):
    return (y2 - y1)

def f(x):
    return 100 * 0.6 ** x

def standardDev(points):
    if len(points) == 1: return points[0]
    return stdev(points)

def megamath(wallet, history):
    if len(history) == 0:
        return 1
    
    subtract = 0
    points1 = [history[0][0] / 100]
    subtract += history[0][0]
    for i in history[1:]:
        points1.append(i[0] / (100 - subtract + 0.05))
        subtract += i[0]
    oppFactor = mean(j for j in points1)
    oppSum = (100 - sum(i[0] for i in history))

    points2 = [history[0][0]]
    for i, j in enumerate(history[1:]):
        points2.append(j[0] / f(i - 1))
    selfFactor = mean(j for j in points2)

    useFactor = selfFactor if standardDev(points2) < standardDev(points1) else oppFactor

    if (oppSum * useFactor + 2 > wallet):
        return 0
    return int(oppSum * (useFactor + 0.1))
    