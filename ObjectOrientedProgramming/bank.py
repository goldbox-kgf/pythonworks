class Bank():
    acc_no=int
    balance=int
    acc_type=str
    customer_name=str

    def __init__(self,acc_no,balance,acc_type,customer_name):
        self.acc_no=acc_no
        self.balance=balance
        self.acc_type=acc_type
        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance+=amount
        print(f" hello {self.customer_name} your account:- {self.acc_no} has been credited with {amount}. your available balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"hello {self.customer_name} account:- {self.acc_no} has been debited with {amount}. your available balance is {self.balance}")
        else:
             print("insufficent balance")
        
    def get_balance(self):
        print("your available balance",self.balance)


bank_instance1=Bank(121,5000,"permanant","chugiyan")

bank_instance1.withdraw(2500)