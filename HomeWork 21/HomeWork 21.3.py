def apply_twice(f, x):
    return f(f(x))

def foo(num):
    return num + 2

res = apply_twice(foo, 3)
print(res) 
