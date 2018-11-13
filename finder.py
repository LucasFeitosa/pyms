from Bio.SeqIO.QualityIO import FastqGeneralIterator
from reader import Config


''' Os primers F tiveram uma taxa de erro ~43% maior que os primers R, proporção similar à dos erros do barcode P1 em relação ao A, reforçando a hipótese de que a taxa de erro no final das sequências é maior. Talvez um próximo passo possa ser verificar como varia o score das bases ao longo da sequência. '''
config = Library("config.txt")
count = 0
total_len = 0

with open("/home/lucas/Documents/micro_antas/R_2018_10_31_14_32_40_user_SN2-1-MacVMic_Auto_user_SN2-1-MacVMic_114.basecaller.fastq") as in_handle:

	flag = 0
	previous_barcode = ''
	for title, seq, qual in FastqGeneralIterator(in_handle):
		count += 1
		total_len += len(seq)
		print(title)
		for barcode_id, barcode in libraries.barcode_library.items():
			if flag == 0:
				if barcode in seq:
					previous_barcode = barcode_id
					print("Found one barcode")
					
		if count == 400:
			break;





#print(libraries)
