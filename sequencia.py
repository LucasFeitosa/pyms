from primer import Primer
from barcode import Barcode
class Sequencia:

	def __init__(self, primer, barcode, seq):
		#print(primer_library)
		#print("Primer: {}".format(primer_library))
		#print("Barcode: {}".format(barcode_library))
		self.primers = primer
		self.barcodes = barcode #tuple de barcode
		self.seq = seq
		#self.motif =  motif
		qualidade = 0

	@property
	def seq(self):
		return self._seq

	@seq.setter
	def seq(self, seq):
		self._seq = seq

	@property
	def primers(self):
		return self._primers

	@primers.setter
	def primers(self, primer_library):
		#print("Primer: {}".format(primer_library))
		self._primers = Primer(primer_library[1][0], primer_library[1][1], primer_library[0])

	@property
	def barcodes(self):
		return self._barcodes

	@barcodes.setter
	def barcodes(self, barcode_library):
		self._barcodes = []
		for i in range(0, len(barcode_library), 2):
			self._barcodes.append(Barcode(barcode_library[i],barcode_library[i+1]))
	#@property
	#def motif(self):
	#	return self._motif

	#@motif.setter
	#def motif(self, motif):
	#	self._motif = motif
