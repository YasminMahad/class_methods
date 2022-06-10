from this import s


class Account :
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
    
    def deposite(self,amount):
        self.balance+=amount
        if amount<=0:
            return f"Deposite must me positive amount"
        else :
            self.balance += amount   
            self.deposits.append(amount) 
            print(self.deposits)
            return f"Your balance is {self.balance}"

    def withdraw(self,amount):
        self.transaction=100
        if amount <=0:
          return f"Hello {self.account_name}, you cannot  withdraw is {amount}"
        
        elif amount>self.balance:
            return f"You can not withdraw {amount} your balance is {self.balance}"
        else:
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)
            print(self.withdrawals)
            return f"Hello {self.account_name}, you have withdrawn {amount}. Your new balance is {self.balance}"
    
    def deposits_statement(self):
        for x in self.deposits:
            print(x,end="\n")
    
    def withdrawals_statement(self):
        for w in self.withdrawals:
            print(w,end="\n")

# Add a method to show the current balance.
    def current_balance(self):
        return self.balance