

class Individuo:
	barcode = ''
	nome = ''
	sequencias = []
	locus = []

	def __init__(self, name = 'Ind', barcode = 'Nobarcode'):
		self.barcode = barcode
		self.nome = name
		self.sequencias = []
		self.locus = []
	def get_barcode(self):
		return self.barcode

	def set_sequencias(self, sequencia):
		self.sequencias.append(sequencia)

	def get_sequencias(self):
		return self.sequencias

	def set_locus(self, locus):
		self.locus.append(locus)

	def get_locus(self):
    return self.locus
