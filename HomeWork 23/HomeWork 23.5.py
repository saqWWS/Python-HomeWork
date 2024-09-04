def read_file_lines(file_path):
    file_path = open(file_path, "r")
    text = file_path.read().splitlines()
    for read_line in text:
        yield read_line


file = "lorem_ipsum.txt"

words_list = read_file_lines(file)
print(next(words_list))
print(next(words_list))
print(next(words_list))
print(next(words_list))
print(next(words_list))
print(next(words_list))
