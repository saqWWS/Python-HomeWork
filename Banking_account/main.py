from Banking_account.account.Account import CheckingAccount, JointAccount, SavingsAccount
from Banking_account.account.Checking_Account import CheckingAccount
from Banking_account.account.SavingsAccount import SavingsAccount
from Banking_account.transfer.Transaction import Transaction
from Banking_account.customer.customer import Customer
from datetime import datetime


def main():
    main_account = CheckingAccount(1234, 500.0, "Checking", 1000.0)
    main_account.deposit(36)
    main_account.withdraw(10)
    main_account.show_balance()
    #
    account_2 = CheckingAccount(1235, 400.0, "Business", 900.0)
    account_2.transfer(main_account, 300)
    account_2.withdraw(30)
    account_2.show_balance()

    saving_account = SavingsAccount(1346, 100, "Savings Account", 0.8)
    saving_account.deposit(10)
    saving_account.apply_interest()
    saving_account.show_balance()
    saving_account.get_account_type()

    owner_account = JointAccount(1237, 100, "Logo", [])
    owner_account.withdraw(4)
    owner_account.add_owner("Iulia")
    owner_account.get_owner()

    transfer_account = Transaction("IRAS", "NRI Account", 962, "transfer", timestamp=datetime.now())
    transfer_account.log()

    Iulias_account_one = CheckingAccount(1238, 300000, "NRI Account", 13000)
    Iulias_account_two = CheckingAccount(1239, 150000, "IRAS", 7500)

    Iulia = Customer("Iulia", "+374858585", [])

    Iulia.add_account(Iulias_account_one)
    Iulia.add_account(Iulias_account_two)
    Iulia.set_name("Iulia")
    Iulia.get_name()
    Iulia.view_accounts()


if __name__ == "__main__":
    main()
