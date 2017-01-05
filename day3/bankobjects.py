
class Bank:
    """
    A simpler, intuitive version of Bank
    """
    def __init__(self):
        self.accounts = []

    def openAccount(self, name):
        newaccount = BankAcct(name)
        self.accounts.append(newaccount)

    def deposit(self, name, amount):
        for bankaccount in self.accounts:
            if bankaccount.name == name:
                bankaccount.removeMoney(amount)
                break # Stop since we found the account

    def transfer(self, fromacct, toacct, amount):
        foundfrom = False
        foundto = False
        for bankaccount in self.accounts:
            if bankaccount.name == fromacct:
                bankaccount.removeMoney(amount)
                foundfrom = True
            if bankaccount.name == toacct:
                bankaccount.addMoney(amount)
                foundto = True
            if foundfrom and foundto:
                break

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
