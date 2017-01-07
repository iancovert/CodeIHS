class Bank:
    def __init__(self, bankName):
        self.accounts = []
        self.name = bankName

    def openAccount(self, name, pin):
        newaccount = BankAcct(name, pin)
        self.accounts.append(newaccount)

    def deposit(self, name, amount, pin):
        for bankaccount in self.accounts:
            if bankaccount.name == name:
                bankaccount.addMoney(amount, pin)

    def withdraw(self, name, amount, pin):
        for bankaccount in self.accounts:
            if bankaccount.name == name:
                bankaccount.removeMoney(amount, pin)

    def __repr__(self):
        return 'Bank: ' + self.name + ' with ' + str(len(self.accounts)) + ' accounts'


class BankAcct:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.credit = 0

    def addMoney(self, amount, pin):
        if pin == self.pin:
            print('Adding money')
            self.credit += amount
        else:
            print('Incorrect pin')

    def removeMoney(self, amount, pin):
        if pin == self.pin:
            print('Removing money')
            self.credit -= amount
        else:
            print('Incorrect pin')

    def __repr__(self):
        return self.name + "'s bank account, balance: " + str(self.credit)


# Test out the Bank class and the BankAcct class

bank = Bank('Bank of Computers')
bank.openAccount('Sumner', 1234)
bank.deposit('Sumner', 100, 1233)
bank.deposit('Sumner', 100, 1234)
bank.openAccount('Pierre', 3333)
bank.deposit('Pierre', 90, 3333)
bank.openAccount('Ian', 9876)
bank.deposit('Ian', 95, 9876)

# Print our the classes (notice how they use the __repr__ functions)

print(bank)
for acct in bank.accounts:
    print(acct)