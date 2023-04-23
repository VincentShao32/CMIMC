def lastOne(wallet, history):
    if len(history) == 0:
        return 0
    return min(wallet, history[-1][0] + 1)
