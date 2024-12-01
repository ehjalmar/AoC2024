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
score = []

for i in range(len(left)):
    hits = 0
    for y in range(len(right)):
        if left[i] == right[y]:
            hits += 1
    print(left[i] * hits)
    score.append(left[i] * hits)

print(sum(score))