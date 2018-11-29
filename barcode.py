

class Barcode():

	def __init__(self, barcodes_id, barcodes_seq):
		#print(barcode_id)
		#print(barcodes_seq)
		self.barcodes_id = barcodes_id
		self.barcodes_seq = barcodes_seq

	def __str__(self):
		return "\n\tBarcode id: {0},\n\tSeq barcode: {1}".format(self.barcodes_id, self.barcodes_seq)

	def __repr__(self):
		return str(self)

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
		self._barcodes_seq = barcodes_seq
