class Account:
	def __init__(self, name, account_number, initial_amount):
		self.name = name
		self.no = account_number
		self.balance = initial_amount
		self.transactions = 0

	def deposit(self, amount):
		self.balance += amount
		self.transactions += 1

	def withdraw(self, amount):
		self.balance -= amount
		self.transactions += 1

	def dump(self):
		s = '%s %s, no. trasactions: %s,  balance: %s' %\
			(self.name, self.no, self.transactions, self.balance)
		print s


def test_Account():
	a1 = Account('John Olsson', '19371554951', 20000)
	a2 = Account('Liz Olsson', '19371564761', 20000)
	a1.deposit(1000)
	a1.withdraw(4000)
	a2.withdraw(10500)
	a1.withdraw(3500)

	success = a1.balance == 20000 + 1000 - 4000 - 3500
	msg = 'Money has dissappeared from first account'
	assert success, msg

	success = a2.balance == 20000 - 10500
	msg = 'Money has dissappeared from second account'
	assert success, msg

	success = a1.transactions == 3
	msg = 'Transactions for first account has not been counted properly'
	assert success, msg

	success = a2.transactions == 1
	msg = 'Transactions for second account has not been counted properly'
	assert success, msg

test_Account()
