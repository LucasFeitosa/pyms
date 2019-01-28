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

=======
#def read_sequences():
config = Config("config.txt")
#print("nope")
count = 0
total_len = 0

sequencias_list = []
sequencias_individuos = {}

with open("R_2018_10_31_14_32_40_user_SN2-1-MacVMic_Auto_user_SN2-1-MacVMic_114.basecaller.fastq") as in_handle:

	count = 0
	flag = False
	previous_barcode = ''
	barcodes = []
	tam_bcode = len(list(config.barcode_config.keys())[0])
	for title, seq, qual in FastqGeneralIterator(in_handle):
		#count += 1
		total_len += len(seq)


			#usando as sequencias dos barcodes como chave do dicionário.
			#função para encontrar o barcode nas seqs
			#função quebrar a sequencia
			#função monta barcodes
			#função monta primers
			#função monta sequencias

			if id_name in sequencias_individuos.keys():


			else:

				sequencias_individuos[ind_name] = seq
			
			#objetos barcode e primer prontos.
			sequence = Sequencia(qual, seq, config)
			barcodes.append(config.barcode_config[seq[:tam_bcode]])
			barcodes.append(seq[:tam_bcode])
			barcodes.append(config.barcode_config[seq[-tam_bcode:]])
			barcodes.append(seq[-tam_bcode:])
			#print(barcodes)


			for primer_id, seq_primer in config.primer_config.items():
				#print(seq_primer)
				if re.search(seq_primer[0], seq) and re.search(seq_primer[1], seq): #consertar a iteração (minimizar o esforço)

					sequencia = Sequencia((primer_id,seq_primer), barcodes, seq)
					#print(sequencia.primers)
					count += 1
					sequencias_list.append(sequencia)
			barcodes = []
		#if count == 400:
		#	break
	print(count)
	#return sequencias_list


def sequence_cleaner(sequence, barcodes, primers):

	sequence, *barcodes = barcode_remover(sequence, barcodes)



def barcode_finder(sequence, barcode_dict):

	if sequence[:tam_bcode] in barcode_dict.keys() and sequence[-tam_bcode:] in barcode_dict.keys():
		ind_name = barcode_dict[seq[:tam_bcode]] + barcode_dict[seq[-tam_bcode:]]
		barcode_one = sequence[:tam_bcode]
		barcode_two = sequence[-tam_bcode:]

	return barcode_one, barcode_two



def barcode_remover(sequence, barcodes):
	print(barcodes)
	barcode_one, barcode_two =  barcode_finder(sequence, barcodes)
	tam_barcode = len(barcode_one)
	clean_barcode_sequence = sequence[tam_barcode:len(sequence) + tam_barcode]

	print(clean_barcode_sequence)
	return clean_barcode_sequence, barcode_one, barcode_two

def primer_finder():

#print(libraries)
