
class BankAccount:
    def __init__(self, balance=0):
        self.balance=balance
        self.int_rate=0.01

    def deposit(self, amount):
        self.balance+= amount
        print(f"Depositing {amount} into your account. New balance is: {self.balance}")
        return self

    def withdraw(self, amount):
        if amount > self.balance :
            self.balance-= amount+5
            print("Insufficient funds: Charging an additional  $5 fee ")
            print(f"Your new balance is {self.balance}")
            return self
        else:
            self.balance-= amount
            print(f"dispensing {amount}, New Balance:{self.balance} ")
            return self

    def display_info(self):
        print(f"Balance is: {self.balance}")
        print(f"Interest Rate: {self.int_rate}")
        return self
        
    def yield_on_int(self):
        
        if self.balance > 0:
            self.balance+=(self.balance*self.int_rate)
            print( f"You balance with Int is {self.balance}")
            return self
        else:
            return print("Your account is empty or over-withdrawn and not accumulating int")

account_1=BankAccount(100)
account_2=BankAccount(100)
account_1.deposit(10).deposit(20).deposit(30).withdraw(50).yield_on_int().display_info()
account_2.deposit(100).deposit(200).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_on_int().display_info()