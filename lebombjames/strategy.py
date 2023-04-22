"""
Edit this file! This is the file you will submit.
"""
import random

totalBoard = []
currBoard = []
lastBoard = []
centres = []
lst = []
grid = []
res = []


def greedy(pid, Board):
    # print(Board)
    global currBoard, lastBoard, grid
    currBoard = Board
    findCrater()
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    updateTotalBoard()
    updateCentres()
    createList()

    global res
    res = []

    for i in range(3):
        addPlacement()


    lastBoard = currBoard
    return res

def findCrater():


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
    tup = lst[1]
    res.append((tup[1], tup[2]))
    totalBoard[tup[1]][tup[2]] += 1

    updateCentres()
    createList()


def updateTotalBoard():
    global totalBoard
    totalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(10)]
    for i in range(len(currBoard)):

        for j in range(len(currBoard[i])):
            for pi in currBoard[i][j]:
                totalBoard[i][j] += pi


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
    strategies = [greedy, random_strategy,
                  random_strategy, random_strategy, strategy]

    return strategies
