import array
from dataclasses import dataclass
from typing import Any, Iterator, Optional


@dataclass(frozen=False)
class DynamicArray:
    def __init__(self, capacity: int = 10):
        self.__capacity = capacity
        self.__size = 0
        self.__array = array.array('i', capacity * [self.__size])

    def re_size(self, new_capacity: int) -> None:
        new_array = array.array('i', [0] * new_capacity)
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def push_back(self, value: int) -> None:
        if self.__size == self.__capacity:
            self.re_size(self.__capacity * 2)
        self.__array[self.__size] = value
        self.__size += 1

    def __len__(self) -> int:
        return self.__size

    def __getitem__(self, index: int) -> Any:
        if index < 0 or index >= self.__size:
            raise IndexError("Index must be positive number!")
        return self.__array[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range!")
        self.__array[index] = value

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = DynamicArray(self.__capacity + other.__size)
        for i in range(self.__size):
            result.push_back(self.__array[i])

        for i in range(other.__size):
            result.push_back(other.__array[i])
        return result

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        for i in range(other.__size):
            self.push_back(other.__array[i])
        return self

    def __repr__(self) -> str:
        return f"{[self.__array[i] for i in range(self.__size)]}"

    def __str__(self) -> str:
        return f"{[self.__array[i] for i in range(self.__size)]}"

    def __eq__(self, other: 'DynamicArray') -> bool:
        if self.__size != other.__size:
            return False
        for i in range(self.__size):
            if self.__array[i] != other.__array[i]:
                return False
        return True

    def __ne__(self, other: 'DynamicArray') -> bool:
        return not self == other

    def __lt__(self, other: 'DynamicArray') -> bool:
        for i in range(min(self.__size, other.__size)):
            if self.__array[i] < other.__array[i]:
                return True
            elif self.__array[i] > other.__array[i]:
                return False
        return self.__size < other.__size

    def __le__(self, other: 'DynamicArray') -> bool:
        return self == other or self < other

    def __gt__(self, other: 'DynamicArray') -> bool:
        return not self <= other

    def __ge__(self, other: 'DynamicArray') -> bool:
        return not self < other

    def __next__(self) -> Any:
        if self._iter_index >= self.__size:
            raise StopIteration
        value = self.__array[self._iter_index]
        self._iter_index += 1
        return value

    def __iter__(self) -> Iterator[Any]:
        self._iter_index = 0
        return self

    def __hash__(self) -> Optional[int]:
        raise TypeError("Mutable type cannot be hashable")


#
#
ls_1 = DynamicArray()
ls_2 = DynamicArray()
ls_3 = DynamicArray()

ls_1.push_back(1)
ls_1.push_back(2)
ls_1.push_back(3)
print(ls_1)

ls_2.push_back(4)
ls_2.push_back(5)
ls_2.push_back(6)
print(ls_2)

ls_3.push_back(7)
ls_3.push_back(8)
ls_3.push_back(9)
print(ls_3)

print(ls_1 + ls_2)
ls_3 += ls_1
print(ls_3)
