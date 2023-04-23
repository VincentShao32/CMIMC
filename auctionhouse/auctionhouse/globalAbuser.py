past_bid = 0

def counterOneMax(wallet, history):
    if len(history) == 0:
        return 0

    global past_bid

    past_bid = min(wallet, max(past_bid + 2, history[-1][0] + 1))

    return past_bid

def counterOneMin(wallet, history):
    if len(history) == 0:
        return 0

    global past_bid

    past_bid = min(wallet, min(past_bid + 2, history[-1][0] + 1))

    return past_bid