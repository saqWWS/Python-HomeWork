from typing import List
from Banking_account.account.Account import Account


class Customer:
    def __init__(self, name: str, contact_info: str, accounts: List[Account]):
        self.set_name(name)
        self.contact_info = contact_info
        self.accounts = accounts

    def add_account(self, account: Account) -> None:
        self.accounts.append(account)

    def set_name(self, person):
        if not isinstance(person, str):
            raise ValueError("Only string!")
        self.name = person

    def get_name(self):
        print(f"Name is: {self.name}")

    def view_accounts(self):
        print(f"{self.name}'s Accounts:")
        for account in self.accounts:
            print(
                f"Account Type: {account.get_account_type()}, Account Number: {account._account_number}, Balance: {account._balance}$")

    def view_transaction_history(self) -> None:
        ...
