from datetime import datetime

class AccountP:
	def __init__(self, name, account_number, initial_amount):
		self._name = name
		self._no = account_number
		#self.balance = initial_amount
		self._transactions = {}
		self.deposit(initial_amount)

	def deposit(self, amount):
		#self.balance += amount
		#self.transactions += 1
		self._transactions[len(self._transactions)] = (datetime.now(), amount)

	def withdraw(self, amount):
		#self.balance -= amount
		#self.transactions += 1
		self._transactions[len(self._transactions)] = (datetime.now(), -amount)

	def get_balance(self):
		balance = 0
		for t in self._transactions:
			balance += self._transactions[t][1]
		return balance

	def get_no_transactions(self):
		return len(self._transactions)

	def dump(self):
		s = '%s %s, no. trasactions: %s,  balance: %s' %\
			(self._name, self._no, self.get_no_transactions(), self.get_balance())
		print s

	def dump_transaction_history(self):
		self.dump()
		for t in sorted(self._transactions):
			s = '%s\t%s' %self._transactions[t]
			print s


def test_AccountP():
	a1 = AccountP('John Olsson', '19371554951', 20000)
	a2 = AccountP('Liz Olsson', '19371564761', 20000)
	a1.deposit(1000)
	a1.withdraw(4000)
	a2.withdraw(10500)
	a1.withdraw(3500)

	#a1.dump()
	#a2.dump()
	a1.dump_transaction_history()
	a2.dump_transaction_history()

	success = a1.get_balance() == 20000 + 1000 - 4000 - 3500
	msg = 'Money has dissappeared from first account'
	assert success, msg

	success = a2.get_balance() == 20000 - 10500
	msg = 'Money has dissappeared from second account'
	assert success, msg

	success = a1.get_no_transactions() == 4
	msg = 'Transactions for first account has not been counted properly'
	assert success, msg

	success = a2.get_no_transactions() == 2
	msg = 'Transactions for second account has not been counted properly'
	assert success, msg

test_AccountP()
