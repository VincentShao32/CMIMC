"""
Edit this file! This is the file you will submit.
"""

# The function called for maze pattern 1


def carnegie_1(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    visited = []
    for time in clock_times:
        visited.append([int((time - 5) / 100), (time - 5) % 100])
    # for wall in walls_horizontal:
    #     print(wall)
    # print()
    # Greedily move up
    steps = 0
    while y + steps < MAZE_SIZE - 1 and steps < 7:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1 or [x, y + steps + 1] in visited:
            break
        steps = steps + 1

    if steps == 0:
        while (y + steps >= 0 and steps > -8):
            if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps] == 1 or [x, y + steps - 1] in visited:
                break
            steps -= 1
    if steps == 0:
        return (0, 38)
    return (steps, 5 + x * 100 + y)

# The function called for maze pattern 2


def carnegie_2(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    # Greedily move up
    steps = 0
    while (y + steps < MAZE_SIZE - 1 and steps < 7):
        if (walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1):
            break
        steps = steps + 1

    return (steps, 5)

# The function called for maze pattern 3


def carnegie_3(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    # Greedily move up
    steps = 0
    while (y + steps < MAZE_SIZE - 1 and steps < 7):
        if (walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1):
            break
        steps = steps + 1

    return (steps, 5)
