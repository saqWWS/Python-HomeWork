import abc


class TransactionManager:
    @abc.abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        ...

    def show_transaction_history(self) -> None:
        ...
