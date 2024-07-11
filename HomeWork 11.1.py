matrix = [[x + (y * 4) for x in range(1, 5)] for y in range(4)]

for i in matrix:
    print(i)
    
print()

row = len(matrix)
column = len(matrix[0])

transposed = [[0] * row for _ in range(column)]


for i in range(row):
    for t in range(column):
        transposed[t][i] = matrix[i][t]

for i in transposed:
    print(i)
