lines=open('day2/input.txt','r').readlines()

validLevels = []
validDiffs = [1,2,3]

for i in range(len(lines)):
    level = list(map(int, lines[i].rstrip().split(" ")))
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
          break
    
    if(is_valid):
        validLevels.append(level)
          
print(len(validLevels))