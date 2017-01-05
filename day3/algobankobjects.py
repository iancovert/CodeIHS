
class Bank:
    """
    This is a much cleaner and faster version of Bank
    """
    def __init__(self):
        self.accounts = {}

    def openAccount(self, name):
        newaccount = BankAcct(name)
        self.accounts[name] = newaccount

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name].addMoney(amount)

    def transfer(self, fromacct, toacct, amount):
        if fromacct in self.accounts and toacct in self.accounts:
            self.accounts[fromacct].removeMoney(amount)
            self.accounts[toacct].addMoney(amount)

def BankAcct:
    def __init__(self, name):
        self.name = name
        self.credit = 0

    def addMoney(self, amount):
        self.credit += amount

    def removeMoney(self, amount):
        self.credit -= amount

    def __repr__(self):
        # A cleaner way to do string concatenation! Look up the format function
        return "({}'s bank account".format(self.name)
