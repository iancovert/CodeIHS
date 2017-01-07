class Cart():
	def __init__(self):
		self.items = []
		self.prices = []
		self.total = 0

	def addItem(self, item, price):
		self.items.append(item)
		self.prices.append(price)
		self.total = self.total + price

	def removeItem(self, item):
		# This is tricky
		index = -1
		for i in range(len(self.items)):
			if self.items[i] == item:
				index = i
		if index > -1:
			self.items.pop(index)
			price = self.prices[index]
			self.prices.pop(index)
			self.total = self.total - price

	def summary(self):
		print('The cart contains:')
		for item in self.items:
			print(item)
		print('Total: ' + str(self.total))


# Test out the shopping cart
cart = Cart()
cart.addItem('apples', 3)
cart.addItem('pasta', 2)
cart.addItem('crackers', 4)
cart.addItem('oranges', 3)
cart.removeItem('apples')
cart.summary()