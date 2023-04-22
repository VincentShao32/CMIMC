def predatorCounter(wallet, history):
    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    if wallet < sum_of_wallet:
        return 0
    else:
        return (sum_of_wallet*0.5 + sum_of_wallet%2) + (1 if sum_of_wallet % 2 == 0 else 0)