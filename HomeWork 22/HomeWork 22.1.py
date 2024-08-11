def file_attributes(file, file_2):
    lines = file.read().splitlines()

    line_count = len(lines)

    print(f"The file has {line_count} lines.")

    file.close()

    word_count = 0
    char_count = 0

    for line in lines:
        tokens = line.split(" ")
        word_count += len(tokens)
        char_count += len(line)

    file_2.write("Lines:" + "\t" + str(line_count) + "\n")
    file_2.write("Words:" + "\t" + str(word_count) + "\n")
    file_2.write("characters:" + "\t" + str(char_count) + "\n")

    print(f"The file has {word_count} words.")
    print(f"The file has {char_count} characters.")

    file_2.close()


file = open("lorem_ipsum.txt", "r")
file_2 = open("lorem_ipsum_2.txt", "w")

file_attributes(file, file_2)
