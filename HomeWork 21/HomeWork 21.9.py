def make_accumulator(start=0):
    res = start
    
    def accumulator(start):
        nonlocal res
        res += start
        return res
    
    return accumulator

result = make_accumulator(3)
print(result(3))  
print(result(5)) 
print(result(7))
