
class Sequencia:
	
	def __init__(self, primer, barcode, f_a, f_b, motif):
		primer = Primer(primer)
		barcode = Barcode(barcode)
		self.flanqueadora_a = f_a
		self.flanqueadora_b = f_b
		self.motif =  motif
		qualidade = 0
		
	@property
	def flanqueadora_a(self):
		return self._flanqueadora_a
	
	@flanqueadora_a.setter
	def flanqueadora_a(self, flanqueadora_a):
		self._flanqueadora_a = flanqueadora_a
		
	@property
	def motif(self):
		return self._motif
	
	@motif.setter
	def motif(self, motif):
		self._motif = motif
