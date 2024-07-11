basic_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
secondary_matrix = [[16 ,15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]



for i in basic_matrix:
    print(i)
    basic_matrix[0] = secondary_matrix[3][::-1] 
    basic_matrix[1] = secondary_matrix[2][::-1]
    basic_matrix[2] = secondary_matrix[1][::-1]
    basic_matrix[3] = secondary_matrix[0][::-1]
    
print()
        
for i in secondary_matrix:
    print(i)
                  
