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
                result = bankaccount.addMoney(amount, pin)
                return result
        return 'Account not found'

    def withdraw(self, name, amount, pin):
        for bankaccount in self.accounts:
            if bankaccount.name == name:
                result = bankaccount.removeMoney(amount, pin)
                return result
        return 'Account not found'

    def __repr__(self):
        return 'Bank: ' + self.name + ' with ' + str(len(self.accounts)) + ' accounts'


class BankAcct:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.credit = 0.

    def addMoney(self, amount, pin):
        if pin == self.pin:
            self.credit += amount
            return 'Success'
        else:
            return 'Incorrect pin'

    def removeMoney(self, amount, pin):
        if pin == self.pin:
            self.credit -= amount
            return 'Success'
        else:
            return 'Incorrect pin'

    def __repr__(self):
        return self.name + "'s bank account, balance: " + str(self.credit)