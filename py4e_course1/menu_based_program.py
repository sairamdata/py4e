# Program to make a simple menu based program.
# 1. Calculator
# 2. Table
# 3. Exit

operators_supported = ['+','-','*','/']

while True:
    print('\nMenu\n1. Calculator\n2. Table \n3. Exit')

    print('\nInput:')
    
    try:
        choice = int(input('Choose option: '))
    except:
        print('Enter a integer choice!!!')
        continue
    
    if choice < 1 or choice > 3:
        print('Enter a valid choice!!!')
        continue
    
    print('Output:')
    if choice == 1:
        print('Calculator selected')
        try:
            first_num = float(input("Enter first number: "))
            get_operator = input("Enter operator (+ - * /): ")
            second_num = float(input("Enter second number: "))
        except:
            print("Enter valid numerical values!!!")
            continue   

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
            
            print("Result:", result)
        else:
            print("Enter valid operators")
    elif choice == 2:
        print('Table selected')
        try:
            number = int(input("Enter a number: "))
        except TypeError:
            print("Enter a integer!!!")
            continue

        for value in range(1, 11):
            print(f'{number} x {value} = {number * value}')
    elif choice == 3:
        print('Thank you for your time!')
        break