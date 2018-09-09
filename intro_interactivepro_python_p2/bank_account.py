class BankAccount:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance
        
    
    def deposit(self, amount):
        #"""Deposits the amount into the account."""
        global total 
        total =self.initial_balance + amount 
        return total 
    
    def withdraw(self, amount):
        
        #Withdraws the amount from the account. Each withdrawal 
        #resulting in a negative balance also deducts a penalty 
        #fee of 5 dollars from the balance.
        global total 
        total = total-amount 
        if total<0:
            total=total-5 
            return total 
        
    def get_balance(self):
        #"""Returns the current balance in the account."""
        global total 
        return total

    #def get_fees(self):
        #"""Returns the total fees ever deducted from the account."""
     
    def __str__(self):
        return "Initial balance: "+str(self.initial_balance)+" and current balance: "+str(total)  

    
my_bankaccount = BankAccount(25)   
my_bankaccount.deposit(25) 
my_bankaccount.withdraw(55)
my_bankaccount.get_balance() 
#print my_bankaccount

