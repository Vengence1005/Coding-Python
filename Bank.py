import sys
class Bank():
    def __init__(self , name,balance = 0.00):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("You dont have sufficient balance")
        else:
            self.balance-= amount
        return self.balance

name = input("Enter your name: ")
b = Bank(name)

while (True):
    print(" d - deposit , w - withdraw , e - exit: ")
    choice = input("")
    if choice == "e" or choice == "E":
        sys.exit()
    else:
        amt = int(input("Enter amount: "))
        if choice == "d" or choice == "D":
            print("{} {} has been deposited in your account".format( name, b.deposit(amt)))
        elif choice == "w" or choice == "W":
            print("{} {} has been withdrawn from your account".format(name, b.withdraw(amt)))
        
