def randomShit(wallet, history):

    if len(history) < 4:
        return 1

    oppSum = 100 - sum(list(map(lambda x: x[0], history)))

    if oppSum * 0.6 > wallet:
        return 0

    return oppSum * 0.5 + 1
