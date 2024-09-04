def is_prime(num: int) -> int:
    for nums in range(num + 1):
        is_ = True
        for i in range(2, int(num ** 0.5) + 1):
            if nums % i == 0:
                is_ = False
                break
        if is_:
            yield nums


prime_nums = is_prime(100)
for item in prime_nums:
    print(item)
