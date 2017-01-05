class Computer:
    # Tell python what this object needs to exist
    # Here, the computer needs an owner
    def __init__(self, owner):
        self.owner = owner
        self.ison = False

    def toggle_power(self):
        self.ison = not self.ison

    def print_owner(self):
        print(self.owner)

alices_computer = Computer("alice")
bobs_computer = Computer("bob")

x = bobs_computer
y = alices_computer

x.print_owner()
y.print_owner()
