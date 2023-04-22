def advay(wallet, history):
    if len(history) < 4:
        return 0

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = sum_of_wallet * 0.50

    return 1 if valid_amount > wallet else valid_amount + 1


def advay2(wallet, history):
    if len(history) < 4:
        return 0

    sumPercs = 0

    total = 100

    for amount, value in history:
        sumPercs = value / total
        total -= amount

    avgPerc = sumPercs / len(history)

    valid_amount = round(total * avgPerc)

    return 0 if valid_amount >= wallet else valid_amount + 1

def ElDesafio(wallet, history):
    if history[-1] == 0 and len(history) < 5:
        return 1

    sum_of_wallet = sum(list(map(lambda x: x[0], history)))
    valid_amount = sum_of_wallet * 0.50

    return 1 if valid_amount > wallet else valid_amount + 1

