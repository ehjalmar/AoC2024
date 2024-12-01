file=open('day1/input.txt','r')
lines=file.readlines()

left = []
right = []

for line in lines:
    splitted_line = line.rstrip().split("  ")
    left.append(int(splitted_line[0]))
    right.append(int(splitted_line[1]))

left.sort()
right.sort()
diffs = []

for i in range(len(left)):
    print(left[i], right[i])
    diffs.append(abs(right[i] - left[i]))

print(sum(diffs))