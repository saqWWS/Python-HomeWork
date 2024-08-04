def bar(n):
    functions = []
    
    for i in range(n):
        def make_multiplier(i):
            def multiplier(x):
                return x * i
            return multiplier
        
        functions.append(make_multiplier(i))
    
    return functions
    
n = int(input("Write a number:\t"))

functions = bar(n)

for i, func in enumerate(functions):
    print(f"Function {i} result with argument 3: {func(3)}")
    print(f"Function {i} closure variables: {[cell.cell_contents for cell in func.__closure__]}")

