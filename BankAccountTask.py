class BankAccount:
    ROI=10.5
    def __init__(self) -> None:
        self.name=""
        self.amount=0
    def accept(self):
        self.name=input("enter the name: ")
        self.amount=int(input("enter the amount: "))
        
    def Deposite(self):
        self.amount+=int(input("enter the amount to deposite: "))
        print("amount deposited successfully........")
    
    def withdraw(self):
        self.amount-=int(input("enter the amount to withdraw: "))
        print("amount withdraw successfully.....")
        
    def CalculateInterest(self):
        intrest=(BankAccount.ROI*self.amount)/100
        print(f'intrest of these amount is {intrest}')
        
PERSON1=BankAccount()
PERSON1.accept()
PERSON1.Deposite()
PERSON1.withdraw()
PERSON1.CalculateInterest()
