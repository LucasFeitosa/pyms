import re
import itertools
from primer import Primer
from barcode import Barcode



def reader(file_name):
	for line in f:

		if "[barcodes]" in line or reading_barcodes:

class Config:

	def __init__(self, file_name):
		self._primer_config = {}
		self._barcode_config = {}
		self.libraries = file_name

	def __str__(self):
		return "Barcodes: {}\nPrimers: {}".format(self.barcode_config, self.primer_config)

	@property
	def libraries(self):
		return self._libraries

	@libraries.setter
	def libraries(self, file_name):
		barcode_list = []
		new_barcode_list = []
		primer_list_f = []
		primer_list_r = []
		reading_barcodes = False
		reading_primers = False
		f = open(file_name, "r")

		for line in f:

			if "[barcodes]" in line or reading_barcodes:
				#print("here")
				if not reading_barcodes:
					line = next(f)
					reading_barcodes = True

				line = line.rstrip().split(" ") #watch out for tabs.


				if len(line) > 1:
					new_barcode_list.append(line)
					print(new_barcode_list)
				else:
					self.barcode_config = new_barcode_list
					reading_barcodes = False


			elif "[primers]" in line or reading_primers:
				if not reading_primers:
					line = next(f)
					#print(line.rstrip().split("_"))
					#print(a)
					if re.match("F", line.rstrip().split("_")[1]):
						previous_orientation = "F"
					elif re.match("R", line.rstrip().split("_")[1]):
						previous_orientation = "R"
					reading_primers = True
				#if "[" not in line:
				#print(line)
				if len(line) > 1:
					current_orientation = line.rstrip().split("_")[1].split(" ")[0]
					#print(current_orientation)
					line = line.rstrip().split(" ")

				if current_orientation == previous_orientation and len(line) > 1:
					if current_orientation == "F":
						primer_list_f.append(line)
					elif current_orientation == "R":
						primer_list_r.append(line)
				else:
					if len(line) > 1:
						if current_orientation == "F":
							primer_list_f.append(line)
						elif current_orientation == "R":
							primer_list_r.append(line)
						previous_orientation = current_orientation
					else:
						reading_primers = False
						self.primer_config = primer_list_f, primer_list_r #watch out for double or more spaces
				#else:
				#	reading_primers = False
				#line = next(f)
				#print(barcode_list)

			#elif "[primers]" in line:
			#	line = next(f)
				#print(line)
			#	while True:



		#print(barcode_list[0])


	@property
	def barcode_config(self):
		return self._barcode_config

	@barcode_config.setter
	def barcode_config(self, barcode_list):
		#key = 1
		for barcode in barcode_list:
			self._barcode_config[barcode[1]] = barcode[0]
		#for r in itertools.product(barcode_list[0], barcode_list[1]):
		#	self._barcode_config[key] = r[0] + r[1] #salva todas as combinações
		#	key += 1
		print(self._barcode_config)

	@property
	def primer_config(self):
		return self._primer_config

	@primer_config.setter
	def primer_config(self, primer_list):
		foward_list = primer_list[0]
		reverse_list = primer_list[1]
		for foward_primer in foward_list:
			#print(foward_primer)
			for reverse_primer in reverse_list:
				if re.match(foward_primer[0][:-1],reverse_primer[0][:-1]):
					#print(reverse_primer)
					self._primer_config[foward_primer[0][:-2]] = [foward_primer[1], reverse_primer[1]]



#Library.barcode_config = "config.txt"
#libraries = Library("config.txt")
#print(libraries.barcode_config)
#print(libraries.primer_config)
