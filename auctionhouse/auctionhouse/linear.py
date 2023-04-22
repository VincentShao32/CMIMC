def f(x):
    return 2 * x + 2


def linear(wallet, history):
    if f(len(history)) > wallet * 0.9:
        return 0
    return int(f(len(history)))
