import copy


def part1(grid) -> int:
    antennas = {}
    # For each postition in the grid, store coordinates in a dictionary
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isalnum():
                current_char = grid[i][j]
                print(current_char, i, j)
                if current_char not in antennas:
                    antennas[current_char] = [(i, j)]
                else:
                    antennas[current_char].append((i, j))
    
    grid_copy = grid.copy()

    # For each antenna, find direction of all other antennas of the same char and store distans in X and Y
    for antenna in antennas:
        for i in range(len(antennas[antenna])):
            for j in range(len(antennas[antenna])):
                if i != j:
                    x_direction = antennas[antenna][j][0] - antennas[antenna][i][0]
                    y_direction = antennas[antenna][j][1] - antennas[antenna][i][1]

                    print("Paired antennas: ", antenna, antennas[antenna][i], antennas[antenna][j], x_direction, y_direction)

                    # Potential anti-node
                    anti_node_1_x = antennas[antenna][i][0] +-x_direction
                    anti_node_1_y = antennas[antenna][i][1] +-y_direction
                    print("Potential anti-node: ", anti_node_1_x, anti_node_1_y)
                    # If within grid, create antinode
                    if anti_node_1_x >= 0 and anti_node_1_x < len(grid_copy[0]) and anti_node_1_y >= 0 and anti_node_1_y < len(grid_copy):
                        grid_copy[anti_node_1_x][anti_node_1_y] = "#"

                    anti_node_2_x = antennas[antenna][j][0] + x_direction
                    anti_node_2_y = antennas[antenna][j][1] + y_direction
                    print("Potential anti-node: ", anti_node_2_x, anti_node_2_y)

                    if anti_node_2_x >= 0 and anti_node_2_x < len(grid_copy[0]) and anti_node_2_y >= 0 and anti_node_2_y < len(grid_copy):
                        grid_copy[anti_node_2_x][anti_node_2_y] = "#"
                    
    # Check how many anti-nodes we have
    anti_nodes = 0
    for row in grid_copy:
        for char in row:
            if char == "#":
                anti_nodes += 1
        
    for row in grid_copy:
        print(''.join(row))
    
    return anti_nodes

def part2(grid) -> int:
    antennas = {}
    # For each postition in the grid, store coordinates in a dictionary
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isalnum():
                current_char = grid[i][j]
                print(current_char, i, j)
                if current_char not in antennas:
                    antennas[current_char] = [(i, j)]
                else:
                    antennas[current_char].append((i, j))
    
    grid_copy = grid.copy()

    # For each antenna, find direction of all other antennas of the same char and store distans in X and Y
    for antenna in antennas:
        for i in range(len(antennas[antenna])):
            for j in range(len(antennas[antenna])):
                if i != j:
                    x_direction = antennas[antenna][j][0] - antennas[antenna][i][0]
                    y_direction = antennas[antenna][j][1] - antennas[antenna][i][1]

                    print("Paired antennas: ", antenna, antennas[antenna][i], antennas[antenna][j], x_direction, y_direction)

                    # Each antenan will also be an anti-node
                    grid_copy[antennas[antenna][i][0]][antennas[antenna][i][1]] = "#"
                    grid_copy[antennas[antenna][j][0]][antennas[antenna][j][1]] = "#"

                    # Potential anti-node
                    anti_node_1_x = antennas[antenna][i][0] +-x_direction
                    anti_node_1_y = antennas[antenna][i][1] +-y_direction

                    while anti_node_1_x >= 0 and anti_node_1_x < len(grid_copy[0]) and anti_node_1_y >= 0 and anti_node_1_y < len(grid_copy):
                        print("Potential anti-node: ", anti_node_1_x, anti_node_1_y)
                        grid_copy[anti_node_1_x][anti_node_1_y] = "#"
                        
                        anti_node_1_x += -x_direction
                        anti_node_1_y += -y_direction

                    anti_node_2_x = antennas[antenna][j][0] + x_direction
                    anti_node_2_y = antennas[antenna][j][1] + y_direction

                    while anti_node_2_x >= 0 and anti_node_2_x < len(grid_copy[0]) and anti_node_2_y >= 0 and anti_node_2_y < len(grid_copy) :
                        print("Potential anti-node: ", anti_node_2_x, anti_node_2_y)
                        grid_copy[anti_node_2_x][anti_node_2_y] = "#"
                        
                        anti_node_2_x += x_direction
                        anti_node_2_y += y_direction
                    
    # Check how many anti-nodes we have
    anti_nodes = 0
    for row in grid_copy:
        for char in row:
            if char == "#":
                anti_nodes += 1
        
    for row in grid_copy:
        print(''.join(row))
    
    return anti_nodes

if __name__ == "__main__":

    lines = open('day8/input.txt','r').readlines()

    # Create 2D array from text input
    grid = []
    for line in lines:
        grid.append(list(line.rstrip()))

    resutl1 = part1(copy.deepcopy(grid))
    result2 = part2(copy.deepcopy(grid))
    
    print("Done!")
    print("PART 1 Antinodes: ", resutl1)
    print("PART 2 Antinodes: ", result2)