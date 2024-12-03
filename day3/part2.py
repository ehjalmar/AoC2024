import re

input = open('day3/input2.txt','r').read()

do_positions = []
for m in re.finditer('do\(\)', input):
    do_positions.append(m.start())

dont_positions = []
for m in re.finditer('don\'t\(\)', input):
    dont_positions.append(m.start())

multiplications = []
last_do = 0
last_dont = -1

for item in re.finditer('mul\(\d+[,]\d+\)', input):
    # check if start of the item is preceded by a 'do' and not a 'don't'
    start_position = item.start()
    for do_position in do_positions:
        if do_position < start_position:
            last_do = do_position
    for dont_position in dont_positions:
        if dont_position < start_position:
            last_dont = dont_position
    
    if last_do > last_dont:
        multiplications.append(item.group(0))

results = []

for i in range(len(multiplications)):
    values = re.findall('\d+', multiplications[i])
    result = int(values[0]) * int(values[1])
    print(result)
    results.append(result)

print("Sum is: " + str(sum(results)))