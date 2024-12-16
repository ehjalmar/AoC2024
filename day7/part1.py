from functools import reduce
from operator import mul
from itertools import product, permutations

if __name__ == "__main__":
    lines = open('day7/input.txt','r').readlines()

    valid_equation_sums = []
    
    for line in lines:
        # extract sum and values
        potential_sum = int(line.split(":")[0])
        values = list(map(int, line.rstrip().split(":")[1].lstrip().split(" ")))

        valid_equation = False
       
        # create possible combinations of operators
        operator = product(["*","+","||"], repeat=len(values)-1)
        operator_combinations = list(operator)

        for ops in operator_combinations:
            current_sum = values[0]
        
            for i in range(len(values)-1):
                if ops[i] == "*":
                    current_sum *= values[i+1]
                elif ops[i] == "+":
                    current_sum += values[i+1]
            
            if current_sum == potential_sum:
                valid_equation = True
        
        if valid_equation:
            valid_equation_sums.append(potential_sum)
            
        print(valid_equation, values)

    print("Valid equations:", len(valid_equation_sums))
    print("Sum of valid equations:", sum(valid_equation_sums))