# Faulty calculator
# Write a program which will correctly solve all the problems except the following ones :-
# 45*3 = 555, 56+9= 77, 56/6=4

"""
print("Type the operator which you want to perform")
operator = input()
print("Enter the operands")
first_operand = int(input())
second_operand = int(input())

if operator == '-':
    print(first_operand ,"-" ,second_operand, "=", first_operand-second_operand)
elif operator == '*':
        if(first_operand==45 and second_operand==3):
            print(first_operand, "*", second_operand, "= 555" )
        else:
            print(first_operand, "*", second_operand, "=", first_operand * second_operand)
elif operator == '+':
    if (first_operand == 56 and second_operand == 9):
        print(first_operand, "+", second_operand, "= 77")
    else:
        print(first_operand, "+", second_operand, "=", first_operand + second_operand)
elif operator == '/':
    if (first_operand == 56 and second_operand == 6):
        print(first_operand, "/", second_operand, "= 4")
    else:
        print(first_operand, "/", second_operand, "=", first_operand / second_operand)
"""

# Faulty calculator
# Write a program which will correctly solve all the problems except the following ones :-
# 45*3 = 555, 56+9= 77, 56/6=4

# Solving Using DICTIONARY

fault_dict={"45*3":"555","56+9":"77","56/6":"4"}

print("Type the operation you wants to perform... like:-  op1 operator op2")
first_operand = input()
operator = input()
second_operand = input()
expression = first_operand + operator + second_operand
reverse = second_operand + operator +first_operand

if expression in fault_dict:
    print(fault_dict[expression])
elif reverse in fault_dict:
    print(fault_dict[reverse])

else:
    print(eval(expression)) # eval() used to evaluate a string by converting it into an expression