def vincent(wallet, history):
    if not history:
        return 8
    # the more rounds, the higher
    # the more losses, the higher
    roundsFactor = 0.005
    lossFactor = 0.1
    opponentWallet = (100 - sum(i[0] for i in history))
    losses = 0
    for i in history:
        if not i[0]: losses += 1
    amount = roundNum(opponentWallet * 0.35)
    return min(wallet, amount - roundNum(lossFactor * losses) * amount + roundNum(roundsFactor * len(history) * amount))

def roundNum(num):
    return round(num * 100) / 100