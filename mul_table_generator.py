# This program takes a numberical integer and prints a
# multiplcation table from 1 to 10.

print("Input:")
try:
    number = int(input("Enter a number: "))
except TypeError:
    print("Enter a integer!!!")
    quit()

for value in range(1, 11):
    print(f'{number} x {value} = {number * value}')