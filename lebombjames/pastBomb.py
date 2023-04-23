
import random

totalBoard = []
currBoard = []
centres = []
lst = []
grid = []
res = []


def seperation(pid, Board):
    global currBoard
    global grid
    currBoard = Board
    grid = [[0] * 10 for i in range(10)]
    updateTotalBoard()
    updateCentres()
    createList()

    global res
    res = []

    addPlacement()
    addPlacement()

    _, x, y = lst[0]

    res.append((abs(9 - x), abs(9 - y)))

    return res


def createList():
    global lst
    lst = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = calcCrossVal(i, j)
            lst.append((grid[i][j], i, j))

    lst = sorted(lst)


def addPlacement():
    global currBoard
    tup = lst[0]
    res.append((tup[1], tup[2]))
    totalBoard[tup[1]][tup[2]] += 1

    updateCentres()
    createList()


def updateTotalBoard():
    global totalBoard
    totalBoard = [[0] * 10 for i in range(10)]
    for i in range(len(currBoard)):

        for j in range(len(currBoard[i])):
            for pi in currBoard[i][j]:
                totalBoard[i][j] += pi


def updateCentres():
    global centres
    centres = [[0] * 10 for _ in range(10)]
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
