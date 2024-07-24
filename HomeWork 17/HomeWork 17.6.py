def fibonacci(num):
        
    fib_sequence = [0, 1]

    while len(fib_sequence) < num:    
        fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(fib)
                
    return fib_sequence

num = int(input("Write a number:\t"))

print(fibonacci(num))
