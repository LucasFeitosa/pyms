import re
from sequencia import Sequencia
from reader import Config
from Bio.SeqIO.QualityIO import FastqGeneralIterator

#def read_sequences():
''' Os primers F tiveram uma taxa de erro ~43% maior que os primers R, proporção similar à dos erros do barcode P1 em relação ao A, reforçando a hipótese de que a taxa de erro no final das sequências é maior. Talvez um próximo passo possa ser verificar como varia o score das bases ao longo da sequência. '''
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
		#print(title)
		 #getting the size of barcode
		#for individuo, barcodes in config.barcode_config.items():
		#print(seq[-tam_bcode:])
		#print(seq[:tam_bcode])
		#print(seq)

		#print(tam_bcode)
		if seq[:tam_bcode] in config.barcode_config.keys() and seq[-tam_bcode:] in config.barcode_config.keys():

			ind_name = config.barcode_config[seq[:tam_bcode]] + config.barcode_config[seq[-tam_bcode:]]

			if id_name in sequencias_individuos.keys():

			else:

				sequencias_individuos[ind_name] = seq
			#barcodes.append(ind_name)
			#barcodes.append(seq[:tam_bcode])
			#barcodes.append(ind_name)
			#barcodes.append(seq[-tam_bcode:])
			#print(ind_name)
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





#print(libraries)
