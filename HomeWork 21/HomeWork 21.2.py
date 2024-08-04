def make_adder(n):
    def adder(x):
        return x + n
    return adder

new_x = make_adder(4)
res = new_x(96)

print(res)