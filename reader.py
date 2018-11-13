import itertools


class Config:

	def __init__(self, file_name):
		self._primer_config = {}
		self._barcode_config = {}
		self.libraries = "config.txt"#file_name

	def __str__(self):
		return "Barcodes: {}\nPrimers: {}".format(self.barcode_config, self.primer_config)
	
	@property
	def libraries(self):
		return self._libraries
	
	@libraries.setter
	def libraries(self, file_name):
		barcode_list = []
		new_barcode_list = []
		reading_barcodes = False
		reading_primers = False
		f = open(file_name, "r")
		
		for line in f:
			
			if "[barcodes]" in line or reading_barcodes:
				print("here")
				if not reading_barcodes:
					line = next(f)
					reading_barcodes = True
					previous_id = line.rstrip().split("_")[0]
			
				
				current_id = line.rstrip().split("_")[0]
				line = line.rstrip().split(" ") #watch out for tabs.
				
				if current_id == previous_id and len(line) > 1:
					
					new_barcode_list.append(line)
					
				else:
					barcode_list.append(new_barcode_list[:])
					if len(line) > 1:
						
						new_barcode_list.clear()
						new_barcode_list.append(line)
						previous_id = current_id
					else:
						reading_barcodes = False
						print("End of barcode reading")
						self.barcode_config = barcode_list
			elif "[primers]" in line or reading_primers:
				if not reading_primers:
					line = next(f)
					reading_primers = True
				#if "[" not in line:
				try:
					#print(line)
					line = line.rstrip().split(" ") #watch out for tabs.
						#print(line)
					
					self.primer_config = line[0], line[1] #watch out for double or more spaces between id and sequence.
				except IndexError:
					reading_primers = False
					print("End of primer reading")
				#else:
				#	reading_primers = False
				#line = next(f)
				#print(barcode_list)
			
			#elif "[primers]" in line:
			#	line = next(f)
				#print(line)
			#	while True:
					
			#		
		#print(barcode_list[0])
				

	@property
	def barcode_config(self):
		return self._barcode_config

	@barcode_config.setter
	def barcode_config(self, barcode_list):
		key = 1
		for r in itertools.product(barcode_list[0], barcode_list[1]): 
			self._barcode_config[key] = r[0] + r[1] #salva todas as combinações
			key += 1
		
	@property
	def primer_config(self):
		return self._primer_config
	
	@primer_config.setter
	def primer_config(self, key_value):
		key, value = key_value
		self._primer_config[key] = value
		
	

#Library.barcode_config = "config.txt"
#libraries = Library("config.txt")
#print(libraries.barcode_config)
#print(libraries.primer_config)

