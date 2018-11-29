import re
from sequencia import Sequencia
from reader import Config
from Bio.SeqIO.QualityIO import FastqGeneralIterator

def read_sequences():
	''' Os primers F tiveram uma taxa de erro ~43% maior que os primers R, proporção similar à dos erros do barcode P1 em relação ao A, reforçando a hipótese de que a taxa de erro no final das sequências é maior. Talvez um próximo passo possa ser verificar como varia o score das bases ao longo da sequência. '''
	config = Config("config.txt")
	count = 0
	total_len = 0
	found_primer = False
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

				if re.match(barcodes[1], seq) and re.match(barcodes[3], seq[-len(barcodes[3]):]):

					for primer_id, seq_primer in config.primer_config.items():

						if re.search(seq_primer[0], seq) and re.search(seq_primer[1], seq): #consertar a iteração (minimizar o esforço)
							primer_library = (primer_id,seq_primer)
							seq = sequence_cleaner((barcodes[1],barcodes[2]),(seq_primer[0], seq_primer[1]), seq)
							sequencia = Sequencia(primer_library, barcodes, seq)
							count += 1
							found_primer = True
							sequencias_list.append(sequencia)
							break

		print(count)
		return sequencias_list


def sequence_cleaner(barcodes, primers, sequence):
	''' Remove barcode and primers from sequences '''
	cleaned_sequence = ''.join(''.join(sequence.split(barcodes[0])).split(barcodes[1]))
	cleaned_sequence = ''.join(''.join(cleaned_sequence.split(primers[0])).split(primers[1]))
	return cleaned_sequence




#print(libraries)
