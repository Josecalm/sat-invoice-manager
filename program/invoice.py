# The two classes are almost identical, due to their basic implementation
# But if more complex operations are ever needed, this approach might
# facilitate the desired implementation.

from person import *

class SalesInvoice:
	receiverRfc = ""
	receiverName = ""
	def __init__(self, date, subtotal, total, rate, tax, receiver):
		self.date = date
		self.receiverRfc = receiver.rfc
		self.receiverName = receiver.name
		self.subtotal = float(subtotal)
		self.total = float(total)
		self.rate = float(rate)
		self.tax = float(tax)

	def __str__(self):
		return ('[' + self.date + '\t' + self.receiverRfc + ' | ' + 
		self.receiverName + ' | $' + str(self.subtotal) + ' | ' + 
		str(self.rate) + ' | $' + str(self.tax) + ' | $' + str(self.total) + ']')

class PurchaseInvoice:
	providerRfc = ""
	providerName = ""
	def __init__(self, date, subtotal, total, rate, tax, provider):
		self.date = date
		self.providerRfc = provider.rfc
		self.providerName = provider.name
		self.subtotal = float(subtotal)
		self.total = float(total)
		self.rate = float(rate)
		self.tax = float(tax)

	def __str__(self):
		return('[' + self.date + '\t' + self.providerRfc + ' | ' + 
			self.providerName + ' | $' + str(self.subtotal) + ' | ' + 
			str(self.rate) + ' | $' + str(self.tax) + ' | $' + str(self.total) + ']')
