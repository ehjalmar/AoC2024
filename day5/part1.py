lines = open('day5/input.txt','r').readlines()

# split in two arrays based on empty line
rules = []
pageupdates = []

while lines:
    line = lines.pop(0)
    if line == '\n':
        break
    rules.append(line.rstrip().split("|"))

while lines:
    line = lines.pop(0)
    pageupdates.append(line.rstrip().split(","))

# Check if pageupdate is valid based on rules
valid_pageupdates = []
for pageupdate in pageupdates:
    current_page_numbers = []
    is_valid = True
    for page_number in pageupdate:
        # check if page_number is in first position of rule anywhere in rules where any of the numbers in current_page_numbers is in the second position
        for rule in rules:
            if page_number == rule[0] and any(x in rule[1] for x in current_page_numbers):
                # print("Invalid page number: " + page_number + " based on rule: " + str(rule))
                is_valid = False
                break
            current_page_numbers.append(page_number)
    
    if is_valid:
        # print("Valid page update: " + str(pageupdate))
        valid_pageupdates.append(pageupdate)

middle_numbers = []
for pageupdate in valid_pageupdates:
    middle_numbers.append(pageupdate[len(pageupdate)//2])

print("Middle numbers: " + str(middle_numbers))    
print("Sum of middle numbers: " + str(sum(map(int, middle_numbers))))
print("Done!")