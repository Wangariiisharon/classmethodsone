class Account: 
    def __init__(self,account_name,balance,account_number):
        self.account_name=account_name
        self.account_number = account_number
        self.balance=balance 

    def deposit(self,amount):
        self.balance+= amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
         
        
           







# Add these methods to class Account -
#  deposit, withdraw. Create two instances of 
#  account and verify they work as expected.
