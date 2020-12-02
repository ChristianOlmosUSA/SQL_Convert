import time 
import csv


filename = '.D:\MY_FILES\Bitcoin_Browser\CSV_to_SQLite\bitcoinAddresses.csv'

print("# len(open(filename).readlines())")
t0 = time.time()
n = len(open(filename).readlines())
print('Elapsed time : ', time.time() - t0)
print('n = ', n)
print('\n')