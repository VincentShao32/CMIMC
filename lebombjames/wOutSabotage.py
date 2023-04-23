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
grid = []
res = []
playerId = 0;

round = 0
players = [0, 0, 0, 0, 0]


# ChaoticCrusaders is a team that uses a spaced out grid pattern. We will implement a sabotage functionality if we detect them
# states = {"twoMinPlayers": False, "hasCrusader"}

def dumbGreedy(pid, Board):
    playerId = pid
    # print(Board)
    global currBoard, lastBoard, grid, round
    currBoard = Board
    # findCrater()
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    updateTotalBoard()
    updateCentres()
    createList()

    global res
    res = []

    for i in range(3):
        # if round > 150 and i == 2:
        #     sabotage()
        # else:
        addSettlement()

    lastBoard = currBoard

    round += 1
    return res


# def findCrater():


def sabotage():
    global players

    sortedPlayers = []
    for i in range(len(players)):
        sortedPlayers.append((players[i], i))

    sortedPlayers = sorted(sortedPlayers, reverse=True)

    toSabotage = -1

    for i in sortedPlayers:
        if i[1] != playerId:
            toSabotage = i
            break

    oppBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]

    for i in range(len(currBoard)):
        for j in range(len(currBoard[i])):
            oppBoard[i][j] = currBoard[i][j][toSabotage] - currBoard[i][j][playerId]

    # maxValX, maxValY, maxVal
    # for i in range(len(oppBoard)):
    #     for j in range(len(oppBoard)):


def createList():
    global lst
    lst = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = calcCrossVal(i, j)
            lst.append((grid[i][j], i, j))

    lst = sorted(lst)


def alreadyPlaced(x, y):
    global res
    # return False
    # if len(res) == 0: testing purposes
    #     return False

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
    totalBoard[tup[1]][tup[2]] += 1

    updateCentres()
    createList()


def updateTotalBoard():
    global totalBoard, players
    players = [0, 0, 0, 0, 0]
    totalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    for i in range(len(currBoard)):
        for j in range(len(currBoard[i])):
            for pi in range(len(currBoard[i][j])):
                totalBoard[i][j] += currBoard[i][j][pi]
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
