
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


class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account=BankAccount(balance=0)

    def make_deposit(self, amount):
        self.account.balance+=amount
        print(f'Your new balance is:{self.account.balance}')

    def make_withdrawl(self, amount):
        if self.account.balance < amount:
            print(f"Insufficient funds, Charging aditional 5$ over withdrawl fee and dispensing ${amount}. Your new balance is {self.account.balance}")
            self.account.balance-= amount+5
        else:
            self.account.balance-= amount
            print(f"dispensing {amount}. YOur new balance is {self.account.balance}")

    def display_bank_account_info(self):
        print(f"Account Balance: {self.account.balance}")

matt=User("Matt", "fcb@gmail")

matt.make_deposit(100)
matt.make_deposit(500)
matt.make_withdrawl(200)
matt.display_bank_account_info()