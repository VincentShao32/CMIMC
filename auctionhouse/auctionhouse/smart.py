def smart(wallet, history):
    if len(history) < 4:
        return 0
    oppSum = (100 - sum(i[0] for i in history))
    losses = 0
    for i in history:
        if not i[0]: losses += 1
    
    if losses == 4:
        if oppSum // 2 + 1 > wallet:
            return  int(oppSum * 0.2 + 1)
        return  oppSum // 2 + 1
    
    return min(wallet, int(oppSum * 0.3 + 1))