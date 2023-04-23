def lastPlusVaried(wallet, history):
    if len(history) == 0:
        return 0
    if history[-1][0] + 2 > wallet * 0.5:
        return 0

    return int(history[-1][0] + 2)
