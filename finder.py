import re
from sequencia import Sequencia
from reader import Config
from Bio.SeqIO.QualityIO import FastqGeneralIterator

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
			#barcodes.append(ind_name)
			#barcodes.append(seq[:tam_bcode])
			#barcodes.append(ind_name)
			#barcodes.append(seq[-tam_bcode:])
			#print(ind_name)
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
