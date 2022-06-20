from datetime import datetime
class Account:   
    def __init__ (self,account_name,account_number):
        self.account_name=account_name
        self.account_number = account_number
        self.balance=0 
        self.deposits=[]
        self.withdrawals=[] 
        self.transaction=100
        self.date=datetime.now().strftime("%x %X")  
        self.fullstatement=[]
        self.loan_balance=0
       


    def deposit(self,amount):   
      
        if amount<=0: 
            return f"Deposit should be more than zero"      
        else: 
             self.balance+=amount 
             self.deposits.append(amount)  
             self.deposits_details={} 
             self.deposits_details["date"]=self.date 
             self.deposits_details["amount"]=amount 
             self.deposits_details["narration"]=f"you have deposited {amount} and your balance is{self.balance}" 
             self.fullstatement.append(self.deposits_details) 
             print(self.deposits)
             return self.deposits_details 
    def deposits_statement(self):  
        for n in self.deposits: 
            print(f"you have deposited {n}") 
    
    def withdraw(self,amount):  
        
        if amount+self.transaction>self.balance: 
            return f"You cannot withdraw more than your balance"
        elif amount<0:  
           
            return f"you cannot withdraw less than zero"   
        elif amount>self.balance: 
            print(f"you cannot withdaw more than your balance")  

        else:  
            self.balance-=amount  
            self.balance-=self.transaction  
            self.withdrawals.append(amount)  
            self.withdrawal_details={} 
            self.withdrawal_details["date"]=self.date 
            self.withdrawal_details[amount]=amount  
            self.withdrawal_details["narration"]=f"you have withdrawn {amount} and your balance is{self.balance}" 
            self.fullstatement.append(self.withdrawal_details)
            return f"You have withdrawn {amount} and your balance is {self.balance}" 

    def withdrawarls_statement(self):
        for i in self.withdrawals: 
            print(f"you have withdrawn {i}")  

    def current_balance(self): 
        return f"your balance is {self.balance} and your transaction fee is {self.transaction}" 

    def full_statement(self): 
        for f in self.fullstatement: 
            time=f["date"] 
            narration=f["narration"]
            amount=f["amount"] 
            print(f"{time}..........{narration}.......{amount}")    



    def borrow(self,amount):
        loan_limit=sum(self.deposits)*1/3 
        interest=0.03*amount 
        number_of_deposit=len(self.deposits)
        self.loan_balance+=(interest +amount) 

       
        if amount>100 and number_of_deposit>=10 and amount<=loan_limit and self.loan_balance==0 and self.balance==0:
            print(f"Hello you have recieved {amount} your loan balance is {self.loan_balance} and your new balance is {amount}") 

        else: 
            print("You are not eligible for a loan")     


    def loan_repayment(self,amount): 
        new_balance=amount-self.loan_balance 
        loan_reduction=self.loan_balance-amount
        if amount>self.loan_balance: 
            print(f"you have overpayed our loan and your balance is {new_balance}") 
        elif amount<self.loan_balance: 
            print(f"You have paid {amount} and your outstanding loan balance is {loan_reduction}")   


    def transfer(self,amount,account_two):
        if amount>self.balance: 
            return f"You do not have sufficient money to transfer{amount}"
        elif amount <= 0:
            return f"Please enter a valid amount"
        else:
            self.balance -= amount
            return f"You have transfered {amount} to {account_two.account_name} your new balance is {self.balance}"
           

         



     
        


    














       
       
# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line 
# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance  
# Add a new method  full_statement which combines both deposits and withdrawals into one list
#  ordered by date and using a for loop prints each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000 
# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.
# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit
# Add a new method transfer which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested 
# amount from the current account to the passed account. The transfer is accomplished by reducing the 
# current account balance and depositing the requested amount to the passed account.

      
           








