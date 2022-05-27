class Account :
    def __init__(self,account_name,account_number,pin,old_balance,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.pin = pin
        self.old_balance = old_balance
        self.balance = balance
    
    def deposite(self):
        self.old_balance += self.balance
        return f"Hello {self.account_name}, your deposite is {self.old_balance}"

    def withdraw(self):
        self.old_balance -= self.balance
        return f"Hello {self.account_name}, your withdrawal is {self.old_balance}"
    