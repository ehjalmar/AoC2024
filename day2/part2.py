lines=open('day2/input.txt','r').readlines()

validLevels = []
validDiffs = [1,2,3]

def check_validity(validDiffs, level):
    diff = level[0] - level[1]
    is_valid = True

    for y in range(len(level) - 1):
        if(diff < 0):
          current_diff = level[y+1] - level[y]
          if(current_diff not in validDiffs):
                is_valid = False
                break
        elif(diff > 0):
          current_diff = level[y] - level[y+1]
          if(current_diff not in validDiffs):
                is_valid = False
                break
        elif(diff == 0):
          is_valid = False
    return is_valid

for i in range(len(lines)):
    level = list(map(int, lines[i].rstrip().split(" ")))
    is_valid = check_validity(validDiffs, level)
    
    if(is_valid):
        validLevels.append(level)
    else: # Try to remove each element and check if it is valid without it
        for y in range(len(level)):
            potential_faulty = level.pop(y)
            is_valid = check_validity(validDiffs, level)
            if(is_valid):
                validLevels.append(level)
                break
            level.insert(y, potential_faulty)
            
            if(is_valid):
              validLevels.append(level)
              break
          
print(len(validLevels))