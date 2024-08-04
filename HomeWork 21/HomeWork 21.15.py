def uppercase(s):
    return text.upper()

def lowercase(s):
    return text.lower()

def titlecase(s):
    return text.title()

def reverse_string(s):
    return text[::-1]

def manipulate_string(s, operation):
    if operation in string_operations:
        return string_operations[operation](s)
    return "There is no such OPERATOR! look carefully!"

string_operations = {
    "big": uppercase,
    "small": lowercase,
    "title": titlecase,
    "reverse": reverse_string
}
operation = input("Enter an operation (big, small, title, reverse):\t").lower()
text = input("Enter a string:\t")

print(manipulate_string(text, operation))