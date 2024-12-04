def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def findWordInDirection(grid, n, m, word, index,
                        x, y, dirX, dirY):
    if index == len(word):
        return True

    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(grid, n, m, word, index + 1, 
                                   x + dirX, y + dirY, dirX, dirY)

    return False

def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    # Directions for 8 possible movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
          
            # Check if the first character matches
            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, 0, 
                                           i, j, dirX, dirY):
                        ans.append([i, j])
                        #break

    return ans

def printResult(ans):
    for a in ans:
       print(f"{{{a[0]},{a[1]}}}", end=" ")
    print()

if __name__ == "__main__":
    lines = open('day4/input.txt','r').readlines()
    # convert the lines to lists of characters
    lines = [list(line.rstrip()) for line in lines]

    word = "XMAS"

    ans = searchWord(lines, word)
    printResult(ans)
    print("Number of occurrences: ", len(ans))