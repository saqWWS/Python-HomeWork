def custom_range(start=0, end=5.5, step=0.5):
    start = start
    end = end
    step = step
    while start != end:
        yield start
        start += step


range_with_float = custom_range()

for num in range_with_float:
    print(num)
