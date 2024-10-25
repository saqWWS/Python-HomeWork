import abc


class Accounts(abc.ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        if not isinstance(account_number, int) or account_number < 0:
            raise ValueError("Must be numbers!")
        self.account_number = account_number
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance cannot be less than zero!")
        self.balance = balance
        if not isinstance(account_type, str):
            raise ValueError("Letters only!")
        self.account_type = account_type

    @abc.abstractmethod
    def deposit(self, amount):
        ...

    @abc.abstractmethod
    def withdraw(self, amount):
        ...


class Customer:
    def __init__(self, name: str, contact_info: str):
        if not isinstance(name, str) or name == "":
            raise ValueError("Letters only!")
        self.name = name
        if not isinstance(contact_info, str) or name == "":
            raise ValueError("Letters only!")
        self.contact_info = contact_info

    def __repr__(self):
        return f"Customer(name={self.name}, contact_info={self.contact_info})"


class Transaction:
    def __init__(self, account: Accounts, amount: float, transaction_type: str):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdrawal':
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")

    def __repr__(self):
        return f"Transaction(account={self.account.account_number}, amount={self.amount}, type={self.transaction_type})"


class CheckingAccount(Accounts):
    def __init__(self, account_number: int, balance: float, account_type: str):
        super().__init__(account_number, balance, account_type)

    def deposit(self, amount: float):
        super().deposit(amount)
        self.balance += amount

    def withdraw(self, amount: float):
        super().deposit(amount)
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __repr__(self):
        return f"Your 'checking account' balance is: {self.balance}"


class SavingsAccount(Accounts):
    def __init__(self, account_number: int, balance: float, account_type: str):
        super().__init__(account_number, balance, account_type)

    def deposit(self, amount: float):
        super().deposit(amount)
        self.balance += amount

    def withdraw(self, amount: float):
        super().withdraw(amount)
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def __repr__(self):
        return f"Your 'savings account' balance is: {self.balance}"


alice = Customer("John Doe", "+374524536")
bob = Customer("John Doe", "+389745896")

checking = CheckingAccount(12, 1000.0, "CheckingAccount")
savings = SavingsAccount(13, 5000.0, "SavingsAccount")

deposit = Transaction(checking, 200.0, "deposit")
withdrawal = Transaction(savings, 150.0, "withdrawal")

deposit.process()
withdrawal.process()

print(checking)
print(savings)
