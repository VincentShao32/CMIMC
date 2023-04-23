def f(x):
    return 3 * x + 4


def linear(wallet, history):
    if f(len(history)) > wallet * 0.9:
        return 0
    return int(f(len(history)))
