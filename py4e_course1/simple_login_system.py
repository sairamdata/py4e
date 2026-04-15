# Program to make a simple login system.

stored_username = 'admin'
stored_password = '1234'

count = 2
username = None
password = None

while count >= 0:
    print("Input:")
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    if username == stored_username and password == stored_password:
        print('Output:')
        print('Login successful')
        break
    else:
        print('Output:')
        print('Incorrect password. Attempts left:', count)
    count -= 1