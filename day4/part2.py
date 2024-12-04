class MAS_Word:
    def __init__(self, x: int, y: int, direction: list):
        self.X = x
        self.Y = y
        self.direction = direction
        
    def __eq__(self, other) -> bool:
        return self.X == other.X and self.Y == other.Y and self.direction == other.direction

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

    # Directions for 4 possible movements
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
          
            # Check if the first character matches
            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, 0, 
                                           i, j, dirX, dirY):
                        ans.append(MAS_Word(i, j, [dirX, dirY]))
                        #break

    return ans

def is_part_of_valid_x(mas_word: MAS_Word, ans):
    
    # If Down and Right
    if mas_word.direction[0] == 1 and mas_word.direction[1] == 1: 
        # Other part of X starts to the right
        right_start = mas_word.X, mas_word.Y+2
        # Check if ans contains an MAS_Word object with coordinates right_start and direction [1, -1]
        if any(foo.X == right_start[0] and
               foo.Y == right_start[1] and
               foo.direction == [1, -1]
                for foo in ans):
            return True, MAS_Word(right_start[0], right_start[1], [1, -1])
        # Other part of X starts below
        below_start = mas_word.X+2, mas_word.Y
        if any(foo.X == below_start[0] and
               foo.Y == below_start[1] and
               foo.direction == [-1, 1]
                for foo in ans):
            return True, MAS_Word(below_start[0], below_start[1], [-1, 1])
        
    # If Down and Left
    elif mas_word.direction[0] == 1 and mas_word.direction[1] == -1:
        # Other part of X starts to the left
        left_start = mas_word.X, mas_word.Y-2
        if any(foo.X == left_start[0] and
               foo.Y == left_start[1] and
               foo.direction == [1, 1]
                for foo in ans):
            return True, MAS_Word(left_start[0], left_start[1], [1, 1])
        # Other part of X starts below
        below_start = mas_word.X+2, mas_word.Y
        if any(foo.X == below_start[0] and
               foo.Y == below_start[1] and
               foo.direction == [-1, -1]
                for foo in ans):
            return True, MAS_Word(below_start[0], below_start[1], [-1, -1])
    
    # If Up and Right
    elif mas_word.direction[0] == -1 and mas_word.direction[1] == 1:
        # Other part of X starts to the right
        right_start = mas_word.X, mas_word.Y+2
        if any(foo.X == right_start[0] and
               foo.Y == right_start[1] and
               foo.direction == [-1, -1]
                for foo in ans):
            return True, MAS_Word(right_start[0], right_start[1], [-1, -1])
        # Other part of X starts above
        above_start = mas_word.X-2, mas_word.Y
        if any(foo.X == above_start[0] and
               foo.Y == above_start[1] and
               foo.direction == [1, 1]
                for foo in ans):
            return True, MAS_Word(above_start[0], above_start[1], [1, 1])
    
    # If Up and Left
    elif mas_word.direction[0] == -1 and mas_word.direction[1] == -1:
        # Other part of X starts to the left
        left_start = mas_word.X, mas_word.Y-2
        if any(foo.X == left_start[0] and
               foo.Y == left_start[1] and
               foo.direction == [-1, 1]
                for foo in ans):
            return True, MAS_Word(left_start[0], left_start[1], [-1, 1])
        # Other part of X starts above
        above_start = mas_word.X-2, mas_word.Y
        if any(foo.X == above_start[0] and
               foo.Y == above_start[1] and
               foo.direction == [1, -1]
                for foo in ans):
            return True, MAS_Word(above_start[0], above_start[1], [1, -1])
        
    return False, None

if __name__ == "__main__":
    lines = open('day4/input.txt','r').readlines()
    # convert the lines to lists of characters
    lines = [list(line.rstrip()) for line in lines]

    word = "MAS"

    ans = searchWord(lines, word)
    
    x_combo = []
    valid_ones = 0
    
    for mas_word in ans:
        is_valid_part, other_leg = is_part_of_valid_x(mas_word, ans)
        if is_valid_part:
            # Check if the combination is already in the list. If not, add it
            if any(foo[0] == other_leg and
                   foo[1] == mas_word
                    for foo in x_combo):
                continue
            if any(foo[0] == mas_word and
                   foo[1] == other_leg
                    for foo in x_combo):
                continue
            
            if is_valid_part:
                x_combo.append([mas_word, other_leg])
                #print((mas_word.X, mas_word.Y), mas_word.direction, (other_leg.X, other_leg.Y), other_leg.direction)
                
                valid_ones += 1


    print("Number of valid Xs: " +  str(valid_ones))