import string

def alphabet():
    return list(string.ascii_lowercase)


def my_zip(*iterables, strict=False):
    
    min_length = min([len(x) for x in iterables])
    
    iterators = [iter(item) for item in iterables]
    res = []
    while True:
        try:
            res.append(tuple([next(item) for item in iterators]))
        except StopIteration:
            break
    return res


def ascci(letters)->tuple:
    
    """
    function is constructed to match
    all lowercase letters, ASCII
    """
    
    ascii_list = []
    
    for letter in letters:
        if isinstance(letter, str):
            ascii_list.append((letter, ord(letter)))
    
    return ascii_list

letters = alphabet()

ascii_alphabet = ascci(letters)

print(tuple(my_zip(ascii_alphabet)))