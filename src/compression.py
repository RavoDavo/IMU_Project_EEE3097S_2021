
import lz4.frame

import time
import sys
from encryption import *
def compress_lz4(path_in):
    global lz4_file
   
    lz4_file=path_in[0:-3]+"lz4" #encrypted_data/encrypted.csv-->encrypted_data/encrypted.lz4
    
    with open(path_in, 'rb') as infile:
    
        with open(lz4_file, 'wb') as outfile:
            tic = time.perf_counter()
            outfile.write(lz4.frame.compress(infile.read(),3))
            toc = time.perf_counter()
            print(f"Compressed the file in {toc - tic:0.4f} seconds")
    encrypt_compress(lz4_file)
           
def decompress_lz4_decrypt(path_out):
    with open(lz4_file, 'rb') as infile:
        with open(path_out, 'wb') as outfile:
            tic = time.perf_counter()
            outfile.write(lz4.frame.decompress(infile.read()))
            toc = time.perf_counter()
            print(f"decompressed the file in {toc - tic:0.4f} seconds")
  
        

