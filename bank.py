class Account: 
    def __init__ (self,account_name,account_number):
        self.account_name=account_name
        self.account_number = account_number
        self.balance=0 
        self.deposits=[]
        self.withdrawals=[] 
        self.transaction=100

    def deposit(self,amount):   
      
        if amount<=0: 
            return f"Deposit should be more than zero"      
        else: 
             self.balance+=amount 
             self.deposits.append(amount) 
             print(self.deposits)
             return f"you have deposited {amount} and your new balance is {self.balance}"
    def deposits_statement(self):  
        for n in self.deposits: 
            print(f"you have deposited {n}") 
    
    def withdraw(self,amount): 
        if amount>self.balance: 
            return f"You cannot withdraw more than your balance"
        elif amount<0:  
           
            return f"you cannot withdraw less than zero"      
        else:  
            self.balance-=amount  
            self.balance-=self.transaction  
            self.withdrawals.append(amount) 
            print(self.withdrawals) 
            return f"You have withdrawn {amount} and your balance is {self.balance}" 

    def withdrawarls_statement(self):
        for i in self.withdrawals: 
            print(f"you have withdrawn {i}")  

    def current_balance(self): 
        return f"your balance is {self.balance} and your transaction fee is {self.transaction}"














       
       
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line 
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance       
           








