

class Barcode(Sequencia):

	def __init__(self, position):

		self.position = position
		self.barcode_seq = barcode_seq

	@property
	def position(self):
		return self._position

	@qual.setter
	def position(self, position):
		self._position = position


'''	def __init__(self, barcodes_id, barcodes_seq):
		#print(barcode_id)
		#print(barcodes_seq)
		self.barcodes_id = barcodes_id
		self.barcodes_seq = barcodes_seq

	def __str__(self):
		return "Barcodes_id: {0},\nSeq: {1}".format(self.barcodes_id, self.barcodes_seq)

	@property
	def barcodes_id(self):
		return self._barcodes_id

	@barcodes_id.setter
	def barcodes_id(self, barcodes_id):
		self._barcodes_id = barcodes_id

	@property
	def barcodes_seq(self):
		return self._barcodes_seq

	@barcodes_seq.setter
	def barcodes_seq(self, barcodes_seq):
		self._barcodes_seq = barcodes_seq'''
