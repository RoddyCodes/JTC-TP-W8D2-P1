class BankAccount:
    
    def __init__(self, accountNumber, accountHolder, initialBalance): 
        self._accountNumber = accountNumber
        self._accountHolder = accountHolder
        self._balance = initialBalance
    def deposit(self, amount): #Method to deposit a specified amount into the account and update the
#balance accordingly.
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount} into account {self._accountNumber}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self._balance:
            print(f"YOU ARE BROKE, CANNOT WITHDRAW")
        else: 
            self._balance -= amount
    def getBalance(self):
        print(self._balance)
    def displayAccountInfo(self):
        print(f"Account Number: {self._accountNumber}")
        print(f"Account Holder: {self._accountHolder}")
        print(f"Current Balance: ${self._balance}")

