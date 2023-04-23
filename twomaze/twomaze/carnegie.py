"""
Edit this file! This is the file you will submit.
"""

# The function called for maze pattern 1


def carnegie_1(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    if len(clock) > 1 and clock_times[-1] != 5 and clock_times[-1] != 38 and walls_horizontal[VIEW_SIZE][VIEW_SIZE + 1] == 1:
        return (0, 5)

    clock = 0
    if clock_times[-1] == 38 and (walls_horizontal[VIEW_SIZE][VIEW_SIZE + 1] == 1 or walls_horizontal[VIEW_SIZE][VIEW_SIZE] == 1):
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + 1] == 1:
            return (-1, 5 + 100 * x + y)
        else:
            return (1, 5 + 100 * x + y)
        clock = 100 * x + y
    visited = set()
    for time in clock_times[1:]:
        if time == 5 or time == 38:
            continue
        t = time - 5
        # print(time)
        point = (int(t / 100) % 100, t % 100)
        t = int(t / 10000)
        visited.add(point)

    # for wall in walls_horizontal:
    #     print(wall)
    # print()
    # print(visited)
    # Greedily move up
    steps = 0
    while y + steps < MAZE_SIZE - 1 and steps < 7:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1 or (x, y + steps + 1) in visited:
            break
        steps = steps + 1

    if steps == 0:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE] != 1 and (x, y - 1) not in visited:
            clock = 100 * x + y
            steps -= 1
    if steps == 0:
        return (0, 38)
    if (x, y) in visited:
        return (steps, 5)
    return (steps, 5 + clock)

# The function called for maze pattern 2


def carnegie_2(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    clock = 0
    if clock_times[-1] == 38 and (walls_horizontal[VIEW_SIZE][VIEW_SIZE + 1] == 1 or walls_horizontal[VIEW_SIZE][VIEW_SIZE] == 1):
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + 1] == 1:
            return (-1, 5 + 100 * x + y)
        else:
            return (1, 5 + 100 * x + y)
        clock = 100 * x + y
    visited = set()
    for time in clock_times[1:]:
        if time == 5 or time == 38:
            continue
        t = time - 5
        # print(time)
        point = (int(t / 100) % 100, t % 100)
        t = int(t / 10000)
        visited.add(point)

    # for wall in walls_horizontal:
    #     print(wall)
    # print()
    # print(visited)
    # Greedily move up
    steps = 0
    while y + steps < MAZE_SIZE - 1 and steps < 7:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1 or (x, y + steps + 1) in visited:
            break
        steps = steps + 1

    if steps == 0:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE] != 1 and (x, y - 1) not in visited:
            clock = 100 * x + y
            steps -= 1
    if steps == 0:
        return (0, 38)
    if (x, y) in visited:
        return (steps, 5)
    return (steps, 5 + clock)

# The function called for maze pattern 3


def carnegie_3(x, y, walls_horizontal, clock_times):
    MAZE_SIZE = 32
    VIEW_SIZE = 8

    visited = set()

    for time in clock_times[1:]:
        if time == 5:
            continue
        t = time - 5
        # print(time)
        point = (int(t / 100) % 100, t % 100)
        visited.add(point)

    steps = 0
    while y + steps < MAZE_SIZE - 1 and steps < 7:
        if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps + 1] == 1 or (x, y + steps + 1) in visited:
            break
        steps += 1
    if steps == 0:
        while y + steps < MAZE_SIZE - 1 and steps > -8:
            if walls_horizontal[VIEW_SIZE][VIEW_SIZE + steps] == 1 or (x, y + steps - 1) in visited:
                break
            steps -= 1
        # while walls_horizontal[VIEW_SIZE][VIEW_SIZE] != 1 and (x, y - 1) not in visited:
        #     clock = 100 * x + y
        #     steps -= 1
    if steps == 0:
        return (0, 5 + 100 * x + y)
    return (steps, 5)
