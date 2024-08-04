def power_factory(num):
    def foo(sec_num):
        return sec_num ** num
    return foo

num = int(input("Write a first number:\t"))
sec_num = int(input("Write a second number:\t"))

new = power_factory(num)
power = new(sec_num)

print(power)