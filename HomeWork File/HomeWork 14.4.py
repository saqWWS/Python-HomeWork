file = open("peterrabbit.txt", mode="r")

read = file.read()
split = read.split()

file.close()

specific_word = ["example", "all", "word", "up", "did", "him"]

count = 0

for i in split:
    if i in specific_word:
        count += 1
                        
print("Specific words", "=", count)
