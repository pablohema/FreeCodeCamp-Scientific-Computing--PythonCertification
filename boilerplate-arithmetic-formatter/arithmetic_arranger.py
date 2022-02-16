def arithmetic_arranger(problems, solution=False):
 # Limit of 4 problems per call
    if len(problems) > 5:
        return "Error: Too many problems."

    # Declaring list to organise problems
    summa1 = []
    summa2 = []
    operator = []

    # Organising problems in right list
    for problem in problems:
        prob_list = problem.split()
        summa1.append(prob_list[0])
        summa2.append(prob_list[2])
        operator.append(prob_list[1])

    # Checking operator
    for char in operator:
        if char != "+" and char != "-":
            return "Error: Operator must be '+' or '-'."

    # Checking digits
    summa_total = []
    summa_total = summa1 + summa2
    for num in summa_total:
        if not num.isdigit():
            return "Error: Numbers must only contain digits."

    # Checking length of digits
    for num in summa_total:
        if len(num) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Solution for summa1, summa. divider and divider
    solution_1 = []
    solution_2 = []
    divider = []
    answer = []

    # solution_1
    for i in range(len(summa1)):
        if len(summa1[i]) > len(summa2[i]):
            solution_1.append(" " * 2 + summa1[i])
        else:
            solution_1.append(" " * (len(summa2[i]) - len(summa1[i])+2) + summa1[i])

    # solution_2
    for i in range(len(summa2)):
        if len(summa2[i]) > len(summa1[i]):
            solution_2.append(operator[i] + " " + summa2[i])
        else:
            solution_2.append(operator[i] + " " * (len(summa1[i]) - len(summa2[i]) + 1) + summa2[i])

    # divider
    for i in range(len(summa1)):
        divider.append("-" * (max(len(summa1[i]), len(summa2[i])) + 2))

    # If solution equals True
    if solution:
        for i in range(len(summa1)):
            if operator[i] == "+":
                sol = str(int(summa1[i]) + int(summa2[i]))
            else:
                sol = str(int(summa1[i]) - int(summa2[i]))

            if len(sol) > max(len(summa1[i]), len(summa2[i])):
                answer.append(" " + sol)
            else:
                answer.append(" " * (max(len(summa1[i]), len(summa2[i])) - len(sol) + 2) + sol)
            arranged_problems = "    ".join(solution_1) + "\n" + "    ".join(solution_2) + "\n" + "    ".join(divider) + "\n" + "    ".join(answer)
    else:
        arranged_problems = "    ".join(solution_1) + "\n" + "    ".join(solution_2) + "\n" + "    ".join(
            divider)

    

    return arranged_problems