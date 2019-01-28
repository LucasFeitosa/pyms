from primer import Primer
from barcode import Barcode
class Sequencia:

	def __init__(self, qual, seq, type, id):

		self.qual = qual
		self.seq = seq
		self.type = type
		self.id = id

	@property
	def qual(self):
		return self._qual

	@qual.setter
	def qual(self, qual):
		self._qual = qual

	@property
	def seq(self):
		return self._seq

	@qual.setter
	def seq(self, seq):
		self._seq = seq

	@property
	def type(self):
		return self._type

	@qual.setter
	def type(self, type, args):
		self._type = type
			#call function to break seq, and ids.

	@property
	def id(self):
		return self._id

	@qual.setter
	def id(self, id):
		self._id = id

'''	def __init__(self, primer, barcode, seq):
		#print(primer_library)
		#print("Primer: {}".format(primer_library))
		#print("Barcode: {}".format(barcode_library))
		self.primers = primer
		self.barcodes = barcode #tuple de barcode
		self.seq = seq
		#self.motif =  motif
		qualidade = 0

	def __str__(self):
		return "\n--------#-----------\nSequence: {0}\nPrimers: {1}\nBarcodes: {2}"\
		.format(self.seq, self.primers, self.barcodes)

	@property
	def seq(self):
		return self._seq

	def __repr__(self):
		return str(self)

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
	#	self._motif = motif '''
