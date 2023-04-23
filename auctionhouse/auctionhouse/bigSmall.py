import random


def bigSmall(wallet, history):
    if len(history) % 2 == 0:
        return int(min(wallet, wallet * random.uniform(0.1, 0.2)))
    return int(min(wallet, wallet * random.uniform(0.5, 0.6)))
