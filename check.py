class bankaccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}, new balance: {self.balance}")

    def display_balance(self):
        print(f"Account number: {self.account_number}, your account balance is {self.balance}")

bank_account = int(input("Enter your bank account number: "))
deposit_amount = int(input("Enter amount to deposit: "))
withdraw_amount = int(input("Enter amount to withdraw: "))

p1 = bankaccount(bank_account)
p1.deposit(deposit_amount)
p1.withdraw(withdraw_amount)
p1.display_balance()