class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Amount Withdrawn")
        else:
            print("Not Enough Balance")

    def balance(self):
        print("Current Balance:", self.__balance)


acc = BankAccount()

acc.deposit(500)
acc.withdraw(300)
acc.balance()