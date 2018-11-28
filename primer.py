

class Primer():

	def __init__(self, forward, reverse, name):



		self.forward = forward
		self.reverse = reverse
		self.name = name

	def __str__(self):
		return "Foward: {0},\nReverse: {1}\n,Name: {2}".format(self.forward, self.reverse, self.name)

	@property
	def forward(self):
		return self._forward

	@forward.setter
	def forward(self, forward):
		self._forward = forward
		#print("Forward {}".format(self._forward))


	@property
	def reverse(self):
		return self._reverse

	@reverse.setter
	def reverse(self, reverse):
		self._reverse = reverse
		#print("Reverse {}".format(self._reverse))

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name
		#print("Name {}".format(self._id))
