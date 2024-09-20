import abc


class Account(abc.ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self._account_number = account_number
        self._balance = balance
        self._account_type = account_type

    @abc.abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        ...

    @abc.abstractmethod
    def show_balance(self) -> None:
        ...

    @abc.abstractmethod
    def get_account_type(self) -> str:
        ...


class CheckingAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, overdraft_limit: float):
        super().__init__(account_number, balance, account_type)
        self._overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        super().deposit(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        self._balance += amount
        print(f"'{self.get_account_type()}' account deposit: {amount}$ New balance: {self._balance}$")

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
            print(f"'{self.get_account_type()}' account withdrew: {amount}$ New balance: {self._balance}$")
        else:
            print("Withdrawal exceeds overdraft limit")

    def transfer(self, destination, amount: float) -> None:
        super().transfer(destination, amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount >= -self._overdraft_limit:
            self._balance -= amount
            destination.deposit(amount)
            print(
                f" Transferred {amount}$ to account {destination.get_account_type()}, new balance 'Business' account: {self._balance}")
        else:
            print("Transfer exceeds overdraft limit, transfer declined.")

    def show_balance(self) -> None:
        print(f"'{self.get_account_type()}' Show Balance: {self._balance}")

    def get_account_type(self) -> str:
        return self._account_type


class SavingsAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, interest_rate: float):
        super().__init__(account_number, balance, account_type)
        self._interest_rate = interest_rate

    def deposit(self, amount: float) -> None:
        super().deposit(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        self._balance += amount
        print(f"'{self.get_account_type()}' account deposit: {amount}$ New balance: {self._balance}$")

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount:
            self._balance -= amount
            print(f"'{self.get_account_type()}' account withdrew: {amount}$ New balance: {self._balance}$")
        else:
            print("Withdrawal exceeds overdraft limit")

    def transfer(self, destination, amount: float):
        super().transfer(destination, amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount:
            self._balance -= amount
            destination.deposit(amount)
            print(
                f" Transferred {amount} to account {destination.get_account_type()}, new balance: {self._balance}")
        else:
            print("Transfer exceeds overdraft limit, transfer declined.")

    def apply_interest(self) -> None:
        interest_amount = self._balance * self._interest_rate
        self._balance += interest_amount
        print(f" Applied interest of {interest_amount:.2f}, New balance: {self._balance:.2f}")

    def show_balance(self) -> None:
        print(f"'{self.get_account_type()}' Show Balance: {self._balance:.2f}")

    def get_account_type(self):
        return self._account_type


class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, account_type: str, joint_owners: list[str]):
        super().__init__(account_number, balance, account_type)
        self.__joint_owners = []

    def deposit(self, amount: float) -> None:
        super().deposit(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        self._balance += amount
        print(f"'{self.get_account_type()}' account deposit: {amount}$ New balance: {self._balance}$")

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount:
            self._balance -= amount
            print(f"'{self.get_account_type()}' account withdrew: {amount}$ New balance: {self._balance}$")
        else:
            print("Withdrawal exceeds overdraft limit")

    def transfer(self, destination, amount: float):
        super().transfer(destination, amount)
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a valid value.")
        if self._balance - amount:
            self._balance -= amount
            destination.deposit(amount)
            print(
                f" Transferred {amount} to account {destination.get_account_type()}, new balance: {self._balance}")
        else:
            print("Transfer exceeds overdraft limit, transfer declined.")

    def show_balance(self) -> None:
        print(f"'{self.get_account_type()}' Show Balance: {self._balance:.2f}")

    def get_account_type(self):
        return self._account_type

    def add_owner(self, customer_name: str) -> None:
        self.__joint_owners.append(customer_name)

    def get_owner(self):
        name = input("Write a your name:\t")
        if name in self.__joint_owners:
            print(f"{self.__joint_owners} is/are an owner of this account.")
        else:
            print(f"'{name}' is not an owner of this account.")
