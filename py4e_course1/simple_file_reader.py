# Program to make a simple file reader.

file_name = input('Enter file name: ')

try:
    file_handle = open(file_name)
except:
    print("File not found!!!")
    quit()

line_count = 0
word_count = 0

for line in file_handle:
    line_count += 1
    words = line.strip().split()
    word_count += len(words)

print('Output:')
print('Lines:', line_count)
print('Words:', word_count)