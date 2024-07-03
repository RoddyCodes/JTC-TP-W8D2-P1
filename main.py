from bank_account import BankAccount
def main():
    #create accounts
    account1 = BankAccount("0000", "jon cena", 3000.0)
    account2 = BankAccount("0001", "da rock", 5000.0)

    #display account info
    account1.displayAccountInfo()
    account2.displayAccountInfo()

    #deposits
    account1.deposit(200.0)
    account2.deposit(200.0)
 
    #withdraws
    account1.withdraw(220.0)
    account2.withdraw(220.0)

    #display new account info
    account1.displayAccountInfo()
    account2.displayAccountInfo()

if __name__ == "__main__":
    main()