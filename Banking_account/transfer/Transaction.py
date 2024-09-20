from Banking_account.account.Account import Account, CheckingAccount, JointAccount, SavingsAccount
from typing import Optional
from datetime import datetime


class Transaction:
    def __init__(self, from_account: 'Account', to_account: Optional['Account'], amount: float,
                 transaction_type: str, timestamp: datetime):
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount
        self._transaction_type = transaction_type
        self._timestamp = timestamp

    def log(self) -> None:
        print(f"Timestamp: {self._timestamp}")
        print(f"Transaction Type: {self._transaction_type}")
        print(f"From Account: {self._from_account} to {self._to_account}")
        print(f"Amount: {self._amount}$")
