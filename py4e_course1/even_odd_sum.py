# Given a sequence of numbers print the count of odd and even
# numbers and the total.

print("Input:")
text = input("Enter numbers (space separated): ")
text = text.split()

for i in range(len(text)):
    text[i] = int(text[i])

even_count = 0
odd_count = 0
total = 0

for number in text:
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    
    total = total + number

print("Output:")
print("Sum:", total)
print("Even count:", even_count)
print("Odd count:", odd_count)