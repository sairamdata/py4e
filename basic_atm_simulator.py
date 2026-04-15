# Program is a simple atm simulator.

balance = 2000

while True:
    print('\nMenu')
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    print('\nInput:')
    try:
        choice = int(input('Choose Option: '))
    except:
        print('Please enter a proper integer choice!')
        continue
    
    if choice < 1 or choice > 4:
        print('Please enter a valid choice!')
        continue

    output_string = ''
    
    if choice == 1:
        output_string = f'Current Balance: {balance}'
    
    elif choice == 2:
        try:
            deposit_amount = int(input('Enter amount: '))
        except:
            print('Enter integer amount!!!')
            continue
        
        if deposit_amount < 0:
            print('Please enter positve deposit amount!')
            continue
        
        balance = balance + deposit_amount
        output_string = f'Deposited sucessfully. Balance {balance}'
    
    elif choice == 3:

        try:
            withdraw_amount = int(input('Enter amount: '))
        except:
            print("Please enter integer amount!!!")
            continue

        if withdraw_amount > balance:
            print('Insufficient Balance!')
            continue
        
        balance = balance - withdraw_amount
        output_string = f'Withdrawn sucessfully. Balance {balance}'
    
    elif choice == 4:
        break

    print(output_string)

print('Thank you for you patronage.')    