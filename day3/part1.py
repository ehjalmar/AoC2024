import re

input = open('day3/input.txt','r').read()
multiplications = re.findall('mul\(\d+[,]\d+\)', input)
#print(result)
results = []

for i in range(len(multiplications)):
    values = re.findall('\d+', multiplications[i])
    result = int(values[0]) * int(values[1])
    print(result)
    results.append(result)

print("Sum is: " + str(sum(results)))