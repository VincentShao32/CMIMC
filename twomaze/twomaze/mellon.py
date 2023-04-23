"""
Edit this file! This is the file you will submit.
"""

# The function called for maze pattern 1


def mellon_1(x, y, walls_vertical, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    visited = []
    for time in clock_times:
        visited.append([int((time - 5) / 100), (time - 5) % 100])
    # print(visited)
    # for wall in walls_vertical:
    #     print(wall)
    # print()
    # Greedily move right
    steps = 0
    while (x + steps < MAZE_SIZE - 1 and steps < 7):
        if walls_vertical[VIEW_SIZE + steps + 1][VIEW_SIZE] == 1 or [x + steps + 1, y] in visited:
            break
        steps = steps + 1
    if steps == 0:
        while (x + steps >= 0 and steps > -8):
            if walls_vertical[VIEW_SIZE + steps][VIEW_SIZE] == 1 or [x + steps - 1, y] in visited:
                break

            steps -= 1
    # print(steps)
    # print([x, y])
    return (steps, 5 + x * 100 + y)

# The function called for maze pattern 2


def mellon_2(x, y, walls_vertical, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    # Greedily move right
    steps = 0
    while (x + steps < MAZE_SIZE - 1 and steps < 7):
        if (walls_vertical[VIEW_SIZE + steps + 1][VIEW_SIZE] == 1):
            break
        steps = steps + 1

    return (steps, 5)

# The function called for maze pattern 3


def mellon_3(x, y, walls_vertical, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    # Greedily move right
    steps = 0
    while (x + steps < MAZE_SIZE - 1 and steps < 7):
        if (walls_vertical[VIEW_SIZE + steps + 1][VIEW_SIZE] == 1):
            break
        steps = steps + 1

    return (steps, 5)
