def loseOpp(wallet, history):
    if len(history) < 4: return 1
    return min(wallet, (100 - sum(i[0] for i in history)) // 2 + 1)