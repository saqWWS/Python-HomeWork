import time


def make_memoize(f):
    cache = {}
    
    def memoized_function(*args):
        if args in cache:
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    
    return memoized_function

args = int(input("Write a number:\t"))

def slow_function(x):
    time.sleep(2)
    return x * x

memoized_slow_function = make_memoize(slow_function)


start_time = time.time()
print(memoized_slow_function(args)) 
print(f"Time taken: {time.time() - start_time} seconds")

start_time = time.time()
print(memoized_slow_function(args)) 
print(f"Time taken: {time.time() - start_time} seconds")
