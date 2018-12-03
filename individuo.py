

class Individuo:

	def __init__(self, identifier, sequencia):
		self.identifier = identifier
		self.sequencias = sequencia

	@property
	def identifier(self):
		return self._identifier

	@identifier.setter
	def identifier(self, identifier):
		self._identifier = identifier

	@property
	def sequencias(self):
		return self._sequencias

	@sequencias.setter
	def sequencias(self, sequencia):
		try:
			self._sequencias.append(sequencia)
		except AttributeError:
			self._sequencias = []
			self._sequencias.append(sequencia)
