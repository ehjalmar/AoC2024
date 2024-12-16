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

        # Find all combinations of values
        operator = product(["*","+","||"], repeat=len(values)-1)
        operator_combinations = list(operator)
        for ops in operator_combinations:
            valid_equation = False
            current_sum = values[0]
            
            for i in range(len(values)-1):
                if ops[i] == "*":
                    current_sum *= values[i+1]
                elif ops[i] == "+":
                    current_sum += values[i+1]
                elif ops[i] == "||":
                    concat_sum = current_sum.__str__() + values[i+1].__str__()
                    current_sum = int(concat_sum)

            if current_sum == potential_sum:
                if potential_sum not in valid_equation_sums:
                    valid_equation_sums.append(potential_sum)
                valid_equation = True
                print(potential_sum, valid_equation, values, ops)            
        

    print("Valid equations:", len(valid_equation_sums))
    print("Sum of valid equations:", sum(valid_equation_sums))