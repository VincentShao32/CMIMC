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
    if history[-1][0] + 1 > wallet * get_percentage(len(history)):
        return 0

    return int(history[-1][0] + 1)
    

def get_percentage(length):
    if length < 3:
        return 0.3
    elif length < 6:
        return 0.5
    elif length < 9:
        return 0.6
    else:
        return 0.7

def logistic_function(x):
    amount = 100 / (1 + math.exp(-0.2 * (x-3)))
    return (100 - amount) / 100