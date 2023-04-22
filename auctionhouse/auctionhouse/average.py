def calcPercent(y, length):
    return (y // 100)**(1/length)

def average(wallet, history):
    oppSum = (100 - sum(i[0] for i in history))

    if len(history) == 0: return int(0.2 * oppSum)
    base = calcPercent(wallet, len(history))
    oppBase = calcPercent(history[-1][0], len(history))
    if oppBase < 0.1:
        return 1
    return min(wallet, oppSum * (oppBase + 0.1))

