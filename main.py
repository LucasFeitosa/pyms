
class Library:

	def __init__(self, file_name):
		self.barcode_library = file_name

	def __str__(self):
		return "{}".format(self.barcode_library)

	@property
	def barcode_library(self):
		print("here")
		return self._barcode_library

	@barcode_library.setter
	def barcode_library(self, file_name):
		f = open(file_name, "r")
		#first_barcode = f.readline().split(" ")[0]
		print("yellow")
		for line in f:
			if "[barcodes]" in line:
				line = next(f)
				while "[" not in line:
					print(line)
					line = line.split(" ")
					self._barcode_library[line[0].split("_")[0]] = line[1]
					line = next(f)

		print(self.barcode_library)

#Library.barcode_library = "config.txt"
tui = Library("config.txt")
print(tui)

