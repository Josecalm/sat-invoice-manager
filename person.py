class Person:
	def __init__(self, name, rfc):
		self.name = name
		self.rfc = rfc

	def __str__(self):
		return ('[' + self.name + ' | ' + self.rfc + ']')