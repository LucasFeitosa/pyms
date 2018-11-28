import re
from sequencia import Sequencia
from reader import Config
from Bio.SeqIO.QualityIO import FastqGeneralIterator

def read_sequences():
	''' Os primers F tiveram uma taxa de erro ~43% maior que os primers R, proporção similar à dos erros do barcode P1 em relação ao A, reforçando a hipótese de que a taxa de erro no final das sequências é maior. Talvez um próximo passo possa ser verificar como varia o score das bases ao longo da sequência. '''
	config = Config("config.txt")
	#print("nope")
	count = 0
	total_len = 0

	sequencias_list = []

	with open("R_2018_10_31_14_32_40_user_SN2-1-MacVMic_Auto_user_SN2-1-MacVMic_114.basecaller.fastq") as in_handle:

		count = 0
		flag = False
		previous_barcode = ''
		for title, seq, qual in FastqGeneralIterator(in_handle):
			#count += 1
			total_len += len(seq)
			#print(title)
			for individuo, barcodes in config.barcode_config.items():
				#print(barcodes[1])
				#print(barcodes[3])
				#for bases in seq:
				if re.match(barcodes[1], seq) and re.match(barcodes[3], seq[-len(barcodes[3]):]):
					#print("Found barcode match")

					for primer_id, seq_primer in config.primer_config.items():
						#print(seq_primer)
						if re.search(seq_primer[0], seq) and re.search(seq_primer[1], seq): #consertar a iteração (minimizar o esforço)
							#print("Found primer match")
							#print(seq_primer)
							#print(seq_primer)
							primer_library = (primer_id,seq_primer)

							sequencia = Sequencia(primer_library, barcodes, seq)
							print(sequencia.primers)
							count += 1
							sequencias_list.append(sequencia)
				#if count == 400:
				#	break
		print(count)
		return sequencias_list





#print(libraries)
