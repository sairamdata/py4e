# This program will tell you if your password is strong
# The condtions to declare a strong password.
# Be >= 8 character
# Contain uppercase
# Contain lowercase
# Contain number
# Contain special character

print("Input:")
password = input("Enter password: ")

password_type = 'Strong'
upper_count = 0
lower_count = 0
space_count = 0
number_count = 0
special_count = 0

for ch in password:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        number_count += 1
    elif ch.isspace():
        space_count += 1
    else:
        special_count += 1

if len(password) <= 8:
    password_type = 'Weak'
elif upper_count == 0:
    password_type = 'Weak'
elif lower_count == 0:
    password_type = 'Weak'
elif special_count == 0:
    password_type = 'Weak'
elif space_count > 0:
    password_type = 'Weak'

print('Output:')
print(password_type, "password")