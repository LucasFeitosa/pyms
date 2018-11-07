
class Library:

	def __init__(self, file_name):
		self._primer_library = {}
		self._barcode_library = {}
		self.libraries = file_name

	def __str__(self):
		return "Barcodes: {}\nPrimers: {}".format(self.barcode_library, self.primer_library)
	
	@property
	def libraries(self):
		return self._libraries
	
	@libraries.setter
	def libraries(self, file_name):
		f = open(file_name, "r")
		for line in f:
			if "[barcodes]" in line:
				line = next(f)
				while True:
					line = line.rstrip().split(" ") #watch out for tabs.
					try:
						self.barcode_library = line[0], line[1] #watch out for double or more spaces between id and sequence.
						line = next(f)
					except IndexError:
						print("End of barcode reading")
						break
			elif "[primers]" in line:
				line = next(f)
				while True:
					
					line = line.rstrip().split(" ") #watch out for tabs.
					#print(line)
					try:
						self.primer_library = line[0], line[1] #watch out for double or more spaces between id and sequence.
						line = next(f)
					except IndexError:
						print("End of primer reading")
						break
				

	@property
	def barcode_library(self):
		return self._barcode_library

	@barcode_library.setter
	def barcode_library(self, key_value):
		#print("here")
		key, value = key_value
		self._barcode_library[key] = value
		#print(self.barcode_library)
	
	@property
	def primer_library(self):
		return self._primer_library
	
	@primer_library.setter
	def primer_library(self, key_value):
		key, value = key_value
		self._primer_library[key] = value
		#print(self._primer_library)
	

#Library.barcode_library = "config.txt"
#libraries = Library("config.txt")
#print(libraries.barcode_library)
#print(libraries.primer_library)

