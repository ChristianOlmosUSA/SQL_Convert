import sqlite3

conn= sqlite3.connect('bitcoinAddresses.sqlite')
cur = conn.cursor()

# How many rows in database? (ie how many bitcoin addresses?)
cur.execute("SELECT max(rowid) from bitcoin")
n = cur.fetchone()[0]
print(n)                    