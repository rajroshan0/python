from math import floor, ceil
import csv
surname="paswan"
sample=[]
with open("sample_"+surname+".csv","r") as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        sample.append(int(row[0]))
        print(sample)


