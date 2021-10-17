#import required module
from cryptography.fernet import Fernet
import csv
import time#opening the key
from compression import *
def decrypt( path_out):
	with open('filekey.key','rb') as filekey:
		key = filekey.read()

	#using the key
	fernet = Fernet(key)

	#opening the encrypted file
	with open('../encrypted_data/encrypted.lz4','rb') as enc_file:
		encrypted = enc_file.read()

	#decrypting the file
	tic = time.perf_counter()
	decrypted = fernet.decrypt(encrypted)
	toc = time.perf_counter()
	#opening the file in write mode and writing the decrypted data
	with open('../decrypted_data/decrypted.lz4','wb') as dec_file:
		dec_file.write(decrypted)
	
	print(f"Decrypted the file in {toc - tic:0.4f} seconds")
	decompress_lz4_decrypt(path_out)
def comparison(file1, file2):
	
	t1 = open(file1, 'r')
	t2 = open(file2, 'r')
	fileone = t1.readlines()
	filetwo = t2.readlines()
	t1.close()
	t2.close()

	
	x = 0
	num=0
	for i in fileone:
		if i != filetwo[x]:
			num+=1
		x += 1
	
	print("There are ",num," differences between original and decrypted file")

