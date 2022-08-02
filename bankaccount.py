# Bank account class

class  BankAccount:

    #init method
    def __init__(self, bal):
        self.__balance = bal
    
    # Method - get balance
    def getBalance(self):
        return self.__balance

    
    # Method - deposit money
    def depositMoney(self, amount):
        self.__balance += amount
    
    # Method - withdraw money
    def withdrawMoney(self, amount):
        if (self.__balance < amount):
            print("Sorry, you don't have sufficient funds, try another amount")
        else:
            self.__balance -= amount