import math

def lastPlusOne(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * 0.:
        return 0

    return int(history[-1][0] + 1)

def lastPlusOneVaried(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 1 > wallet * logistic_function(len(history)):
        return 0

    return int(history[-1][0] + 1)
    

def logistic_function(x):
    amount = 100 / (1 + math.exp(-0.2 * x))
    return (100 - amount) / 100