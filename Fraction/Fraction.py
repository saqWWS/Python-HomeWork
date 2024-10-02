from __future__ import annotations
from dataclasses import dataclass
from math import gcd


@dataclass(frozen=False)
class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        common_divisor = gcd(numerator, denominator)
        self.set_Numerator(numerator // common_divisor)
        self.set_Denominator(denominator // common_divisor)

    def set_Denominator(self, value: int) -> None:
        if value == 0:
            raise ValueError("Denominator cannot be zero.")
        if not isinstance(value, int):
            raise ValueError("You cannot use the string type.")
        self.__denominator = value

    def set_Numerator(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("You cannot use the string type.")
        self.__numerator = value

    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.__numerator}, {self.__denominator})"

    def __not_valid(self, value) -> None:
        if not isinstance(value, int):
            return self, value

    def __add__(self, other) -> int:
        if self.__not_valid(other):
            new_form_one = self.__numerator * other.__denominator + self.__denominator * other.__numerator
            new_form_two = self.__denominator * other.__denominator
            return Fraction(new_form_one, new_form_two)

    def __sub__(self, other) -> int:
        if self.__not_valid(other):
            new_form_one = self.__numerator * other.__denominator - self.__denominator * other.__numerator
            new_form_two = self.__denominator * other.__denominator
            return Fraction(new_form_one, new_form_two)

    def __mul__(self, other) -> int:
        if self.__not_valid(other):
            new_form_one = self.__numerator * other.__numerator
            new_form_two = self.__denominator * other.__denominator
            return Fraction(new_form_one, new_form_two)

    def __truediv__(self, other) -> int:
        if self.__not_valid(other):
            new_form_one = self.__numerator * other.__denominator
            new_form_two = self.__denominator * other.__numerator
            return Fraction(new_form_one, new_form_two)

    def __eq__(self, other) -> bool:
        if self.__not_valid(other):
            equal = self.__numerator == other.__numerator and self.__denominator == other.__denominator
            return equal

    def __ne__(self, other) -> bool:
        if self.__not_valid(other):
            not_equal = not self.__numerator == other.__numerator and not self.__denominator == other.__denominator
            return not_equal

    def __lt__(self, other) -> bool:
        if self.__not_valid(other):
            less_then = self.__numerator * other.__denominator < self.__denominator * other.__numerator
            return less_then

    def __le__(self, other) -> bool:
        if self.__not_valid(other):
            less_or_equal = self.__numerator * other.__denominator <= self.__denominator * other.__numerator
            return less_or_equal

    def __gt__(self, other) -> bool:
        if self.__not_valid(other):
            greater_than = self.__numerator * other.__denominator > self.__denominator * other.__numerator
            return greater_than

    def __ge__(self, other) -> bool:
        if self.__not_valid(other):
            greater_or_equal = self.__numerator * other.__denominator >= self.__denominator * other.__numerator
            return greater_or_equal

    def __hash__(self) -> int:
        if self.__not_valid(self):
            new_hash = hash((self.__numerator, self.__denominator))
            return new_hash

    def __float__(self) -> float:
        if self.__not_valid(self):
            float_div = self.__numerator / self.__denominator
            return float_div

    def __int__(self) -> int:
        if self.__not_valid(self):
            truncating_div = self.__numerator // self.__denominator
            return truncating_div

    def __neg__(self) -> None:
        if self.__not_valid(self):
            return Fraction(-self.__numerator, self.__denominator)

    def to_mixed_number(self) -> str:

        num = self.__numerator // self.__denominator
        value = abs(self.__numerator) % self.__denominator
        if value == 0:
            return str(num)
        return f"{num} {value}/{self.__denominator}"

    def __iadd__(self, other) -> int:
        add = other + self
        return add

    def __isub__(self, other) -> int:
        sub = other - self
        return sub

    def __imul__(self, other) -> int:
        mul = other * self
        return mul

    def __itruediv__(self, other) -> int:
        div = other / self
        return div


f1 = Fraction(3, 4)
f2 = Fraction(2, 3)

print(f"f1: {f1}")
print(f"f2: {f2}")

print()

print(f"f1 + f2: {f1 + f2}")
print(f"f1 - f2: {f1 - f2}")
print(f"f1 * f2: {f1 * f2}")
print(f"f1 / f2: {f1 / f2}")

print()

print(f"f1 equal (==) f2: {f1 == f2}")
print(f"f1 > (less then) f2: {f1 > f2}")
print(f"f1 < (great then) f2: {f1 < f2}")
print(f"f1 >= (less or equal) f2: {f1 >= f2}")
print(f"f1 <= (great or equal) f2: {f1 <= f2}")

print()

fraction_dict = {f1, f2, Fraction(3, 4)}
print(f"Keys and Values: {fraction_dict}")

print()

print(f"f1 is: {float(f1)}")
print(f" f1 is: {int(f1)}")
print(f"Negative: {f1.__neg__()}")

print()

f3 = Fraction(7, 4)
print(f"Mixed: {f3.to_mixed_number()}")

print()

f1 += f2
print(f"f1 += f2: {f1}")
f1 -= f2
print(f"f1 -= f2: {f1}")
f1 *= f2
print(f"f1 *= f2: {f1}")
f1 /= f2
print(f"f1 /= f2: {f1}")
