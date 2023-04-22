def yanda(wallet, history):
    oppwallet = 100
    for i in history:
        oppwallet -= i[0]
    
    if oppwallet > wallet:
        return 0
    else:
        return (0.5*oppwallet + oppwallet%1) + 1