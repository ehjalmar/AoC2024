import copy
from multiprocessing import Pool, Manager
import time

from tqdm import tqdm

def move_in_direction(grid, current, direction):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    next_position = (current[0] + direction[0], current[1] + direction[1])
    
    # return if we´re out of bounds
    out_of_grid = next_position[0] < 0 or next_position[0] >= len(grid) or next_position[1] < 0 or next_position[1] >= len(grid[next_position[0]])

    if out_of_grid:
        return current, direction, out_of_grid

    if grid[next_position[0]][next_position[1]] == "#":
        if direction == directions[0]:
            direction = directions[3]
        elif direction == directions[1]:
            direction = directions[0]
        elif direction == directions[2]:
            direction = directions[1]
        elif direction == directions[3]:
            direction = directions[2]

    else:
        current = next_position
    
    return current, direction, out_of_grid

def check_for_loop(args):
    grid, start, i, j = args
    grid_copy = copy.deepcopy(grid)
    grid_copy[i][j] = "#"
    traveled_from_to = []
    current = start
    direction = (-1, 0)
    out_of_grid = False
    while not out_of_grid and (current[0] < len(grid_copy) and current[1] < len(grid_copy[current[0]])) and grid_copy[current[0]][current[1]] != "#" and current[0] >= 0 and current[1] >= 0:
        # Move to the next position
        from_position = current
        current, direction, out_of_grid = move_in_direction(grid_copy, current, direction)
        to_position = current
        if (from_position, to_position, direction) in traveled_from_to:
            return 1
        else:
            traveled_from_to.append((from_position, to_position, direction))
    
    return 0

if __name__ == "__main__":
    start_time = time.process_time()
    # create 2D array from text input
    lines = open('day6/input.txt','r').readlines()
    grid = []
    for line in lines:
        grid.append(list(line.rstrip()))

    # Find starting point of char "^"
    start = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                start = (i, j)
                break
        else:
            continue
        break

    # Find the path
    path = []
    current = start
    direction = (-1, 0)
    out_of_grid = False
    # Walk until we reach the end of the grid or we reach the char "#"
    while not out_of_grid and current[0] < len(grid) and current[1] < len(grid[current[0]]) and grid[current[0]][current[1]] != "#" and current[0] >= 0 and current[1] >= 0:
        # Add current position to path
        path.append(current)
        # Move to the next position
        current, direction, out_of_grid = move_in_direction(grid, current, direction)
        
    # Simulate a # blocker in each postion in the grid(where we don´t already have a # or the start postion "^")
    positions_to_check = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "^":
                continue
            positions_to_check.append((i, j))

    blockers_found = 0
    tasks = [(grid, start, i, j) for i, j in positions_to_check]
    with Pool() as p:
        blockers_found = list(tqdm(p.imap(check_for_loop, tasks), total=len(tasks)))

    # print distinct positions
    print("Unique visited positions: " +  str(len(set(path))))
    #print("Possible blockers to create a loop: " + str(len(possible_blockers)))
    print("Blockers found: " + str(sum(blockers_found)))
    endtime = time.process_time() - start_time
    print("Execution time: " + str(endtime))