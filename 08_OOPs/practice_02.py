# Create Account class with 2 attributes balance & account no. create methods for debit ,credit  & printing the balance.

class Account:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance :",self.balance)
        
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credit")
        print("total balance :",self.balance)
        
A1 = Account(12345,10000)
A1.debit(5000)
A1.credit(6000)
A1.debit(7000)
A1.credit(40000)