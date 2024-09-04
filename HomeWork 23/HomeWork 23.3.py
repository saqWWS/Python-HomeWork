def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


endless_process = infinite_sequence()
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))
print(next(endless_process))

for i in infinite_sequence():
    if i == 11:
        break
    print(i, end=" ")
