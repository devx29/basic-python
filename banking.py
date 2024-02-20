class BalanceException(Exception):
    pass

class Banking:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def balance(self):
        print(f"\n{self.account} Account Balance : ${self.amount:.2f}")

    def deposit(self, deposit_amount):
        print(f"\nDeposit of ${deposit_amount:.2f} received")
        self.amount += deposit_amount
        self.balance()

    def valid_transaction(self, deposit_amount):
        if self.amount >= deposit_amount:
            return
        else:
            # self.balance()
            raise BalanceException("\nAmount exceeds current balance")
        
    def withdrawal(self, withdrawal_amount):
        try:
            self.valid_transaction(withdrawal_amount)
            print(f"\nWithdrawal of ${withdrawal_amount:.2f} complete")
            self.amount -= withdrawal_amount
            self.balance()
        except BalanceException as error:
             print(f"\nWithdrawal Incomplete! {error}") 

checking = Banking("Checking", 5000)
savings = Banking("Savings", 10000)

checking.balance()
savings.balance()
checking.deposit(1000)
savings.withdrawal(2500)
checking.withdrawal(7500)

