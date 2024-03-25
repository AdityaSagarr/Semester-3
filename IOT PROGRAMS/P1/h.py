# h) Read File and Print Word Count:
with open("sample.txt", "r") as MY_F:
    for line in MY_F:
        words = line.split()
        word_count = len(words)
        print("Word count:", word_count)