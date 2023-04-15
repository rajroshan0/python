# order of task 2 & 3
from random import randint, seed
import csv # imorted csv package to create a csv file
seed()
surname="paswan.roshan"
#lets generate a sample 
sample = [randint(1,43) for i in range(30)]
print(sample)

with open("sample_"+surname+".py","w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in sample:
        csv_writer.writerow([item])
# order of task 4
import math
from math import floor , ceil

print (math.floor(23.424))
print (math.ceil(3534.453))
# order of task 4
surname = "rajroshan"

sample = []
with open("sample_"+surname+".csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        sample.append(int(row[0]))
        print(sample)
        print()
#no of interval

        range_num=8

