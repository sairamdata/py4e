# When user inputs any text, the program counts the number of words.

print("Input:")
text = input("Enter a sentence: ")

text_words = text.split()
word_count = len(text_words)
character_count = len(text)

print("Output:")
print("Word count:", word_count)
print("Chracter count:", character_count)
