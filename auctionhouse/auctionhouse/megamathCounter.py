def randomShit(wallet, history):

    if len(history) < 4:
        return 1

    oppSum = 100 - sum(list(map(lambda x: x[0], history)))

    if oppSum * 0.5 + 1 > wallet:
        return 0

    return min(oppSum * 0.5 + 1, wallet)
