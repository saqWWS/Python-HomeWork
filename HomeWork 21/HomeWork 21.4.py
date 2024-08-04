def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

def foo(num):
    return num + 1

def fn(num):
    return num * num

comp_func = compose(fn, foo)
res = comp_func(3)
print(res)  
