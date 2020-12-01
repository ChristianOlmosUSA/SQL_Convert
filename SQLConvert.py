
import sqlite3          # to set up: pip install db-sqlite3
import csv              # to set up: pip install python-csv

conn= sqlite3.connect('bitcoinAddresses.sqlite')    # Calling our SQL file: bitcoinAddresses
cur = conn.cursor()             # something about connecting to the SQL file

cur.execute('DROP TABLE IF EXISTS bitcoin')     # if already run this table exists - consider renaming and just look for newly added addresses?
cur.execute('''
CREATE TABLE "bitcoin"(
    "Public_Address_base58" TEXT,
    "Satoshis" TEXT,
    "Block" TEXT,
    "hexRIPEMD160" TEXT
) 
''')                # Create an SQL table

fname=input("Enter name of CSV file to convert: ")
if len(fname) < 1 : fname = "bitcoinAddresses.csv"          # if you just press enter it looks for this default file name

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')        # ensure the , is your delimiter else change this
    for row in csv_reader:
        print(row)              # this loops yur csv and prints to SQL
        Public_Address_base58=row[0]
        Satoshis=int(row[1])
        Block=int(row[2])
        HexRIPEMD160=row[3]
        cur.execute('''INSERT INTO bitcoin(Public_Address_base58,Satoshis,Block,HexRIPEMD160) VALUES(?,?,?,?)''',(Public_Address_base58,Satoshis,Block,HexRIPEMD160))
        conn.commit()