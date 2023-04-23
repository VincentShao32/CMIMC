
def sabotage():
    # print("begin")
    global sortedPlayers

    toSabotage = ()
    for i in sortedPlayers:
        if i[1] != playerId:
            toSabotage = i
            break

    oppBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]

    for i in range(len(currBoard)):
        for j in range(len(currBoard[i])):
            oppBoard[i][j] = currBoard[i][j][toSabotage[1]] - currBoard[i][j][playerId]

    maxValX = -1
    maxValY = -1
    maxVal = -1

    for i in range(len(oppBoard)):
        for j in range(len(oppBoard)):
            total = oppBoard[i][j]
            if i < 9:
                total += oppBoard[i + 1][j]
            if j < 9:
                total += oppBoard[i][j + 1]
            if i > 0:
                total += oppBoard[i - 1][j]
            if j > 0:
                total += oppBoard[i][j - 1]
            if total > maxVal:
                maxVal = total
                maxValX = i
                maxValY = j

    topTwo = []

    for i in reversed(lst):
        if not (i[1] == maxValX and i[2] == maxValY):
            topTwo.append(i)
        else: #could fix structure of code so that the maxVal found earlier can't be one of these two. This doesn't sabotage when it sometimes should
            addSettlement()
            return

    if (topTwo[1][0] - centres[maxValX][maxValY] == 0) and maxVal > 2:
        # print("sabotaging")
        res.append((maxValX, maxValY))
        totalBoard[maxValX][maxValY] += 1
        updateCentres()
        createList()
    else:
        addSettlement()