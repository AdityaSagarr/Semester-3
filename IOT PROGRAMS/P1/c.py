# c) Word and Character Count:
usx_input = input("Enter a string: ")
split_string = usx_input.split()
word_count = 0
char_count = 0
for word in split_string:
    word_count += 1
    for char in word:
        char_count += 1
print("Total words:", word_count)
print("Total characters:", char_count)