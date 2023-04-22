from statistics import mean

def calcSlope(y2, y1):
    return (y2 - y1)

def megamath(wallet, history):
    if len(history) == 0:
        return 1
    
    subtract = 0
    points = [history[0][0] / 100]
    subtract += history[0][0]
    for i in history[1:]:
        points.append(i[0] / (100 - subtract + 0.05))
        subtract += i[0]
    # points += [history[i][0] // (100 - subtract) for i, j in enumerate(history[1:])]
    # slope = mean(calcSlope(j, points[i - 1]) for i, j in enumerate(points[-3:]))
    factor = mean(j for j in points)
    oppSum = (100 - sum(i[0] for i in history))

    if (oppSum * factor + 2 > wallet):
        return 0
    return int(oppSum * (factor + 0.1))
    