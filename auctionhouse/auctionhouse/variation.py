import random


def variation(wallet, history):
    rand = random.randint(0, 10)
    if rand <= 3:
        return 4
    return 10
