def advay(wallet, history):
    if len(history) < 3:
        return 0

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = sum_of_wallet * 0.60

    return 1 if valid_amount > wallet else valid_amount + 1
