from statistics import mean, median


def average(wallet, history):
    if not history:
        return 0
    amount = mean(i[0] for i in history)
    if amount > wallet * 0.5:
        return 0
    return amount


def med(wallet, history):
    if not history:
        return 0
    amount = median(i[0] for i in history)
    if amount > wallet * 0.5:
        return 0
    return amount
