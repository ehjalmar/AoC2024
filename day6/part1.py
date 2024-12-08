if __name__ == "__main__":
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
    direction = "up"
    # Walk until we reach the end of the grid or we reach the char "#"
    while current[0] < len(grid) and current[1] < len(grid[current[0]]) and grid[current[0]][current[1]] != "#" and current[0] >= 0 and current[1] >= 0:
        # Add current position to path
        path.append(current)
        # Move to the next position
        if direction == "up":
            if current[0] - 1 >= 0 and grid[current[0] - 1][current[1]] == "#":
                direction = "right"
                current = (current[0], current[1] + 1)
            else:
                current = (current[0] - 1, current[1])
        elif direction == "right":
            if current[1] + 1 < len(grid[current[0]]) and grid[current[0]][current[1] + 1] == "#":
                direction = "down"
                current = (current[0] + 1, current[1])
            else:
                current = (current[0], current[1] + 1)
        elif direction == "down":
            if current[0] + 1 < len(grid) and grid[current[0] + 1][current[1]] == "#":
                direction = "left"
                current = (current[0], current[1] - 1)
            else:
                current = (current[0] + 1, current[1])
        elif direction == "left":
            if current[1] - 1 >= 0 and grid[current[0]][current[1] - 1] == "#":
                direction = "up"
                current = (current[0] - 1, current[1])
            else:
                current = (current[0], current[1] - 1)
        
    # print distinct positions
    print(len(set(path)))

    print("Done!")