import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Account:
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance
    def debit(self,x):
        self.balance-=x
        print(f"Your A/C ({self.accno}) has been debited BDT {x}. Avl balance: BDT {self.balance}")
    def credit(self,x):
        self.balance+=x
        print(f"Your A/C ({self.accno}) has been credited BDT {x}. Avl balance: BDT {self.balance}")
    def prt(self):
        print("Your current balance is ",self.balance,"BDT")

ob1=Account(2204034, 10600)
ob1.prt()
ob1.debit(2000)
ob1.credit(10000)