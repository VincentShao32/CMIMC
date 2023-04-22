def loseUs(wallet, history):
    if len(history) < 5: return 0
    return int(wallet * 0.3)