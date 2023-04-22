import math


def advay(wallet, history):
    if len(history) < 4:
        return 0

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = sum_of_wallet * 0.50

    return 1 if valid_amount > wallet else valid_amount + 1


def advay2(wallet, history):
    if len(history) < 4:
        return 0

    sumPercs = 0

    total = 100

    for amount, value in history:
        if total == 0:
            break
        sumPercs = value / total
        total -= amount

    avgPerc = sumPercs / len(history)

    valid_amount = round(total * avgPerc)

    return 0 if valid_amount >= wallet else valid_amount + 1


def logistic_function(x):
    amount = 100 / (1 + math.exp(-0.04 * x))
    return (100 - amount) / 100


def ElDesafio(wallet, history):
    if len(history) == 0:
        return 0

    if history[-1] == 0 and len(history) < 5:
        return 1

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = int(sum_of_wallet * 0.50)

    return 0 if valid_amount > wallet else valid_amount + 1


def ElDesafisimo(wallet, history):
    if len(history) == 0:
        return 0

    if history[-1] == 0 and len(history) < 5:
        return 1

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = sum_of_wallet * logistic_function(len(history))

    return 1 if valid_amount > wallet else valid_amount + 1
