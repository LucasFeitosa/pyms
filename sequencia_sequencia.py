

class Sequencia_sequencia(Sequencia):

	def __init__(self, barcode, primer):

		self.barcode = barcode
		self.primer = primer

	@property
	def barcode(self):
		return self._barcode

	@qual.setter
	def barcode(self, barcode):
		self._barcode = barcode

	@property
	def primer(self):
		return self._primer

	@qual.setter
	def primer(self, primer):
		self._primer = primer
