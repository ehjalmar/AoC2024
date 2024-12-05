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

# Get non valid pageupdate based on rules
non_valid_pageupdates = []
for pageupdate in pageupdates:
    is_valid = True
    needs_reordering = True
    while needs_reordering:
            current_page_numbers = []
            needs_reordering = False
            for page_number in pageupdate:
                # check if page_number is in first position of rule anywhere in rules where any of the numbers in current_page_numbers is in the second position
                for rule in rules:
                    if page_number == rule[0] and any(x in rule[1] for x in current_page_numbers):
                        # print("Invalid page number: " + page_number + " based on rule: " + str(rule))
                        # Re-order the pageupdate based on the rule
                        pageupdate.remove(page_number)
                        new_index = pageupdate.index(rule[1])
                        pageupdate.insert(new_index, page_number)
                        needs_reordering = True
                        is_valid = False
                        break

                    current_page_numbers.append(page_number)
    
    if not is_valid:
        # print("Non valid page update: " + str(pageupdate))
        non_valid_pageupdates.append(pageupdate)

middle_numbers = []
for pageupdate in non_valid_pageupdates:
    middle_numbers.append(pageupdate[len(pageupdate)//2])

print("Middle numbers: " + str(middle_numbers))    
print("Sum of middle numbers: " + str(sum(map(int, middle_numbers))))
print("Done!")