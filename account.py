from datetime import datetime
from time import strftime


class Account :
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.statement = []
        self.transaction = {}
        self.loan_balance = 0
        
    
    def deposite(self,amount):
        self.balance += amount
        time = strftime("%c")
        narration = "You have deposited successfully"
        self.transaction={amount, time,narration}
        if amount<=0:
            return f"Deposite must be positive amount"
        else :  
            self.deposits.append(amount)
            return f"{self.transaction} Your balance is {self.balance}"

    def withdraw(self,amount):
        self.amount += amount
        transaction_fee=100
        time = strftime("%c")
        to_withdraw = self.amount + transaction_fee
        narration = "You have withdrawn successfully"
        self.transaction = {amount,time,narration}
        if amount <=0:
          return f"Hello {self.account_name}, you cannot  withdraw your amount is {amount}"
        
        elif amount>self.balance:
            return f"You can not withdraw {amount} your balance is {self.balance}"
        else:
            self.balance-=to_withdraw
            self.withdrawals.append(amount)
            print( f"Hello {self.account_name}, you have withdrawn {amount}. Your new balance is {self.balance}, and your withdrawals are {len(self.withdrawals)}")
            print(self.transaction)
    def deposits_statement(self):
        for x in self.deposits:
            print(x,end="")
    
    def withdrawals_statement(self):
        for w in self.withdrawals:
            print(w,end="")
        
# Add a method to show the current balance.
    def current_balance(self):
        return self.balance

    def full_statement(self):
        for money_transaction in self.statement:
            amount=money_transaction["amount"]
            Narration=money_transaction["Narration"]
            time=money_transaction["time"]
            date=time.strftime("%x/%X")
            print(f"{date}: {Narration} {amount}")
    def transfer(self,receiver,amount):
        self.receiver=receiver
        self.amount=amount
        current_balance=self.balance-amount
        if amount<=0:
            print( f"You cannot transfer a non-existant amount")
        elif amount>self.balance:
            print(f"Your cannot transfer {amount}.Your current balance is {self.balance}")
        elif amount<self.balance:
            print(f"You have transfered {amount} to {self.receiver} your current balance is {current_balance}")
    def  borrow_loans(self,loan_amount):
            self.loan_amount=loan_amount
            self.interest=0.03*self.loan_amount
            self.total_loan=self.loan_amount+self.interest
            if len(self.deposits)>10 and loan_amount<=sum(self.deposits)//3 and loan_amount>100 and self.balance<0:
                print(f"You have been awarded a loan of {loan_amount} your current balance is {self.amount}")
            else:
                print("You are not eligible for a loan")

    def pay_loans(self,amount_payloan):
              self.amount_payloan=amount_payloan
              self.interest=0.03*self.loan_amount
              total_topay=amount_payloan+self.interest
              
              loan_remaining=self.loan_amount-amount_payloan
              new_balance=self.loan_amount-total_topay
              if total_topay>0:
                  print(f"You have deposited {amount_payloan} your loan of {self.loan_amount}Ksh.Your new loan balance is {new_balance}Ksh")
              elif total_topay>loan_remaining:
                  print(f"Congratulations!! You have cleared your loan of {self.amount}.Your new balance is{new_balance}")
              else:
                  print(f"You have a loan balance of {self.total_loan}")

    def current_balance(self):
             print(f"Your current balance {self.balance}Ksh" )
                               
