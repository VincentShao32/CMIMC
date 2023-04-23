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

#ChaoticCrusaders is a team that uses a spaced out grid pattern. We will implement a sabotage functionality if we detect them
# states = {"twoMinPlayers": False, "hasCrusader"}

def greedy(pid, Board):
    global currBoard, lastBoard,  round, playerId
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
        addSettlement()

    lastBoard = currBoard

    round += 1

    if len(res) == 2:
        print("TWO")

    for i, j in res:
        if i >= 0 and i <= 9 and j >=0 and j<=9:
            continue
        print("INVALID")

    return res

# def findCrater():

def updatePlayerStandings():
    global players, sortedPlayers
    sortedPlayers = []
    for i in range(len(players)):
        sortedPlayers.append((players[i], i))

    sortedPlayers = sorted(sortedPlayers, reverse=True)

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



def createList():
    global lst
    lst = []

    for i in range(10):
        for j in range(10):
            lst.append((calcCrossVal(i, j), i, j))

    lst = sorted(lst)


def alreadyPlaced(x, y):
    global res
    if len(res) == 0:
        return False

    for i in res:
        if math.sqrt(math.pow(x - i[0], 2) + math.pow(y - i[1], 2)) <= 2:
            return True

    return False

def addSettlement():
    global currBoard
    pool = []
    for i in range(int(len(lst))):
        if alreadyPlaced(lst[i][1], lst[i][2]):
            continue
        else:
            pool.append(lst[i])


    # tup = pool[random.randint(0, len(pool) - 1)]

    tup = pool[0]
    res.append((tup[1], tup[2]))
    totalBoard[tup[1]][tup[2]] += 1 #changed

    updateCentres()
    createList()


def updateTotalBoard():
    global totalBoard, players
    players = [0, 0, 0, 0, 0]
    totalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    for i in range(len(currBoard)):
        for j in range(len(currBoard[i])):
            for pi in range(len(currBoard[i][j])):
                totalBoard[i][j] += currBoard[i][j][pi]  #changed if pi == playerId else currBoard[i][j][pi]
                players[pi] += currBoard[i][j][pi]


def updateCentres():
    global centres
    centres = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    for i in range(len(centres)):
        for j in range(len(centres[i])):
            centres[i][j] = calcCentres(i, j)


def calcCentres(x, y):
    total = 0
    # print(len(totalBoard))
    # print(str(x) + " " + str(y))
    total += totalBoard[x][y]
    if x < 9:
        total += totalBoard[x + 1][y]
    if y < 9:
        total += totalBoard[x][y + 1]
    if x > 0:
        total += totalBoard[x - 1][y]
    if y > 0:
        total += totalBoard[x][y - 1]

    return total


def calcCrossVal(x, y):
    total = 0
    total = centres[x][y]
    if x < 9:
        total = max(total, centres[x + 1][y])
    if y < 9:
        total = max(total, centres[x][y + 1])
    if x > 0:
        total = max(total, centres[x - 1][y])
    if y > 0:
        total = max(total, centres[x][y - 1])
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
    strategies = [greedy, random_strategy, random_strategy, random_strategy, strategy]

    return strategies
