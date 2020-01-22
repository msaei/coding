#4thought
#https://open.kattis.com/problems/4thought

def calculate(operators):
    #first path do the * and /
    prev = 4
    acc = 0
    for operator in operators:
        if operator == '+':
            acc += prev
            prev = 4
        elif operator == '-':
            acc += prev
            prev = -4
        elif operator == '*':
            prev = prev * 4
        elif operator == '/':
            prev = prev // 4
    acc += prev
    return acc
def display(operators , n):
    print('4', operators[0], '4', operators[1], '4', operators[2], '4 =', n)
def isPossible(n):
    operators = ['+', '-', '*', '/']
    combinations = []
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                if calculate([op1, op2, op3]) == n:
                    display([op1, op2, op3], n)
                    return
    print("no solution")
    return

        
        
for _ in range(int(input())):
    isPossible(int(input()))

