def f(x):
    return 0.07 * (x - 3)


def g(x):
    return 1.05 ** (x - 2) - 1


def lastPlusMultiple(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 2 > wallet * min(1, (0.3 + f(len(history)))):
        return 0
    return int(history[-1][0] + 2)


def lastPlusMultipleExp(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * min(1, (0.4 + g(len(history)))):
        return 0
    return int(history[-1][0] + 1)
