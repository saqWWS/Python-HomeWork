def repeat_element(element, times):
    new_elements = [element] * times
    for item in new_elements:
        yield item


num_for_element = int(input("Write a element:\t"))
num_for_times = int(input("Write how many times:\t"))
several_times = repeat_element(num_for_element, num_for_times)
print(next(several_times), end=" ")
print(next(several_times), end=" ")


