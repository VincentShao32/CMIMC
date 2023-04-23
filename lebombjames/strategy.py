"""
Edit this file! This is the file you will submit.
"""
import random
import math

totalBoard = []
currBoard = []
lastBoard = []
centres = []
lst = []
res = []
playerId = 0

round = 0
players = [0, 0, 0, 0, 0]
sortedPlayers = []

# ChaoticCrusaders is a team that uses a spaced out grid pattern. We will implement a sabotage functionality if we detect them
# states = {"twoMinPlayers": False, "hasCrusader"}


def greedy(pid, Board):
    global currBoard, lastBoard, round, playerId
    playerId = pid
    currBoard = Board
    # findCrater()
    updateTotalBoard()
    updatePlayerStandings()
    updateCentres()
    createList()

    global res
    res = []

    for i in range(3):
        # if round > 150 and i == 0 and getPlayerDiff() < 0.1:
        #     sabotage()
        # else:
        addSettlement()

    lastBoard = currBoard

    round += 1

    # if len(res) == 2:
    #     print("TWO")

    return res

# def findCrater():


def updatePlayerStandings():
    global players, sortedPlayers
    sortedPlayers = sorted(((player, i)
                           for i, player in enumerate(players)), reverse=True)
    # sortedPlayers = []
    # for i in range(len(players)):
    #     sortedPlayers.append((players[i], i))

    # sortedPlayers = sorted(sortedPlayers, reverse=True)


def getPlayerDiff():
    global sortedPlayers, playerId
    ownScore = ()
    maxVal = 0
    for i in sortedPlayers:
        if i[1] == playerId:
            ownScore = i
            break
        else:
            maxVal = max(maxVal, i[0])

    # print(playerId)
    # print(sortedPlayers)
    return 1.0 - maxVal/ownScore[0]


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
            oppBoard[i][j] = currBoard[i][j][toSabotage[1]] - \
                currBoard[i][j][playerId]

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
        else:  # could fix structure of code so that the maxVal found earlier can't be one of these two. This doesn't sabotage when it sometimes should
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


def createList():
    global lst
    lst = []

    for i in range(10):
        for j in range(10):
            lst.append((calcCrossVal(i, j), i, j))

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         grid[i][j] = calcCrossVal(i, j)
    #         lst.append((grid[i][j], i, j))

    lst = sorted(lst)


def alreadyPlaced(x, y):
    global res
    if not res:
        return False

    for i in res:
        if math.sqrt((x - i[0]) ** 2 + (y - i[1]) ** 2) <= 2:
            return True

    return False


def addSettlement():
    global currBoard
    pool = []
    for i in lst:
        if alreadyPlaced(i[1], i[2]):
            continue
        else:
            pool.append(i)

    # tup = pool[random.randint(0, len(pool) - 1)]

    tup = pool[0]
    res.append((tup[1], tup[2]))
    totalBoard[tup[1]][tup[2]] += 1  # changed

    updateCentres()
    createList()


def updateTotalBoard():
    global totalBoard, players
    players = [0 for i in range(5)]
    totalBoard = [[0 for i in range(10)] for i in range(10)]
    for i, r in enumerate(currBoard):
        for j, c in enumerate(r):
            for pi, p in enumerate(c):
                totalBoard[i][j] += p
                players[pi] += p
    # for i in range(len(currBoard)):
    #     for j in range(len(currBoard[i])):
    #         for pi in range(len(currBoard[i][j])):
    #             # changed if pi == playerId else currBoard[i][j][pi]
    #             totalBoard[i][j] += currBoard[i][j][pi]
    #             players[pi] += currBoard[i][j][pi]


def updateCentres():
    global centres
    centres = [[0 for i in range(10)] for i in range(10)]
    for i, r in enumerate(centres):
        for j, c in enumerate(r):
            centres[i][j] = calcCentres(i, j)
    # for i in range(len(centres)):
    #     for j in range(len(centres[i])):
    #         centres[i][j] = calcCentres(i, j)


def calcCentres(x, y):
    total = 0
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, 1, 0, -1]
    for xC, yC in zip(dx, dy):
        r = x + xC
        c = y + yC
        if r > 9 or r < 0 or c > 9 or c < 0:
            continue
        total += totalBoard[x + xC][y + yC]

    # print(len(totalBoard))
    # print(str(x) + " " + str(y))
    # total += totalBoard[x][y]
    # if x < 9:
    #     total += totalBoard[x + 1][y]
    # if y < 9:
    #     total += totalBoard[x][y + 1]
    # if x > 0:
    #     total += totalBoard[x - 1][y]
    # if y > 0:
    #     total += totalBoard[x][y - 1]

    return total


def calcCrossVal(x, y):
    total = 0
    total = centres[x][y]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for xC, yC in zip(dx, dy):
        r = x + xC
        c = y + yC
        if r > 9 or r < 0 or c > 9 or c < 0:
            continue
        total = max(total, centres[x + xC][y + yC])
    # if x < 9:
    #     total = max(total, centres[x + 1][y])
    # if y < 9:
    #     total = max(total, centres[x][y + 1])
    # if x > 0:
    #     total = max(total, centres[x - 1][y])
    # if y > 0:
    #     total = max(total, centres[x][y - 1])
    return total

# Implement me!


def strategy(pid, board):
    return [(0, 0), (0, 0), (0, 0)]

# A random strategy to use in your game.


def random_strategy(pid, board):
    return [
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
        (random.randint(0, 9), random.randint(0, 9)),
    ]

# Edit me!


def get_strategies():
    """
    Returns a list of strategy functions to use in a game.

    In the local tester, all of the strategies will be used as separate players in the game.
    Results will be printed out in the order of the list.

    In the official grader, only the first element of the list will be used as your strategy. 
    """
    strategies = [greedy, random_strategy,
                  random_strategy, random_strategy, strategy]

    return strategies
