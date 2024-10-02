class ValidatedString:
    def __init__(self, length):
        self.__length = length

    def __get__(self, instance, owner):
        return instance.val

    def __set__(self, instance, value):
        if len(value) <= self.__length:
            raise ValueError(f"String length must be greater than {self.__length} characters.")
        instance.val = value


class User:
    username = ValidatedString(length=3)

    def __init__(self, username):
        self.username = username


try:
    alice = User("Alice")
    print(alice.username)
    bob = User("Bob")
    print(bob.username)
except ValueError as e:
    print(f"Exception caught: {e}")
