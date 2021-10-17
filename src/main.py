from compression import *
from decryption import *
import time
import os
path_in="../IMU_Data/IMU_Data.csv"

path_out="../Output_Data/IMU_Data_Out.csv"
tic = time.perf_counter()
compress_lz4(path_in)
decrypt(path_out)
toc = time.perf_counter()

comparison(path_in, path_out)
print(f"The total runtime is {toc - tic:0.4f} seconds (including reading and writing to files)")
x=os.stat(path_in).st_size
y=os.stat(path_in[0:-3]+"lz4").st_size
print(f"Uncompressed size: ",x)
print(f"Compressed size: ",y)