# This is a simple calculator program for practice.
import sys

operators_supported = ['+','-','*','/']

print("Input:")

try:
    first_num = float(input("Enter first number: "))
    get_operator = input("Enter operator (+ - * /): ")
    second_num = float(input("Enter second number: "))
except:
    print("Enter valid numerical values!!!")
    sys.exit()    

result = None
if get_operator in operators_supported:
    if get_operator == '+':
        result = first_num + second_num
    elif get_operator == '-':
        result = first_num - second_num
    elif get_operator == '*':
        result = first_num * second_num
    elif get_operator == '/':
        result = first_num / second_num
    
    if result - int(result) == 0:
        result = int(result)
    
    print('Output:')
    print("Result:", result)
else:
    print("Enter valid operators")