def f(x):
    return 0.1 * x

def linear(wallet, history):
    return int(min(wallet, f(len(history)) * wallet))