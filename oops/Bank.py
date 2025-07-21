# Create a bank account class that have two 
# attributes owner and balance.and two methods 
# deposit withdrawal 
# Withdrawal may not exceed the available balance

class bank_account():

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,credit):
        self.balance+=credit
        print("Amount {} credited successfully \n Available balance of {} : {}".format(credit,self.owner,self.balance))

    def withdraw(self,debit):
        if(debit>self.balance):
            print("Insufficient balance ): ")
        else:
            self.balance-=debit
            print("amount {} debited successfully \n Available balance of {} : {}".format(debit,self.owner,self.balance))
    
    def check(self):
        print("Available balance of {} : {}".format(self.owner,self.balance))

    
mPass=bank_account(owner='bidhan',balance=5000)

mPass.deposit(100)
mPass.withdraw(200)
mPass.withdraw(5000)



        

