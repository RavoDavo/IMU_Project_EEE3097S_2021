#import required module
from cryptography.fernet import Fernet

import time
def encrypt_compress(path_in):
	#key generation
	key = Fernet.generate_key()

	#string the key in a file. Generates a file with the name filekey.key
	with open('filekey.key','wb') as filekey:
		filekey.write(key)

	#encrypting this file
	#opening the key
	with open('filekey.key','rb') as filekey:
		key = filekey.read()

	#using the generated key
	fernet = Fernet(key)

	#opening the original file to encrypt
	with open(path_in,'rb') as file: #'nbaa.csv' is the name of the csv file that was being read. Edit this to the name of the file you would like to read
		original = file.read()

	#encrypting the file
	tic = time.perf_counter()
	encrypted = fernet.encrypt(original)
	toc = time.perf_counter()
	#opening the file in write mode and writing the encypted dat
	with open('../encrypted_data/encrypted.lz4','wb') as encrypted_file: #'nbaResult.csv' is the name of the file that contains the encrypted data. You can change this if you want
		encrypted_file.write(encrypted)
	
	print(f"Encrypting the file took {toc - tic:0.4f} seconds")
	
	



