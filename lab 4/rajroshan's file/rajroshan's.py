from random import randint, seed
from math import ceil,floor
import csv
seed()
surname="rajroshan"
sample =[randint(1,31) for i in range(40)]
print(sample)
print()
with open("sample_"+surname+".csv","w",newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in sample:
        csv_writer.writerow([item])
 
surname="rajroshan"
sample=[]
with open('sample_'+surname+ ".csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        sample.append(int(row[0]))
print(sample)
print()
ranges_num = 8
    sample_sorted = sorted(sample)
    print('sample_sorted is ', sample_sorted)
    freqs = []
    for el in set(sample_sorted):
        freqs.append(sample_sorted.count(el))
        print("data output")
        print("output")
        for x in set(sample):
            divider = " | "
            if x < 10:
                shift = " "
            else:
                shift = ""
            print (shift,x,divider,sample.count(x))
            print()

            min_smpl =min(sample_sorted)
            max_smpl =max(sample_sorted)
            range_values = max_smpl - min_smpl


            len_int = range_values / ranges_num
            if len_int - floor(len_int) < 0.5:
                len_int = floor(len_int)                    
            else:
                len_int = ceil(len_int)
            print("output: yes", ranges_num)
            print("dlta intereva:" , len_int)
            print()

            print("minimum: ", min_smpl)
            print("maximum: ",max_smpl)# upto here no problem
            print("dignosis chooe :", range_values)
            for i in range(min_smpl, max_smpl, len_int):
               bottom_bounds.appent(i)
               upper_bounds=[]
               for i in range(1,len(bottom_bounds)):
                   upper_bounds.append(bottom_bounds[i] - 1)
               last_bottom_bound= bottom_bounds[len(bottom_bounds) - 1]
               upper_bounds.append.appned(last_bottom_bound + len_int - 1)
               prop_bottom_bounds = list()
               prop_upper_bounds.append(i-0.5)
               prop_upper_bounds.append(j+0.5)

               intfreq = list|()
               for bot,up in zip(prop_bottom_bounds,prop_upper_bounds):
                   counter = 0
                   for i in sample_sorted:
                        if bot < i < up:
                           counter += 1
                   int_freq.append(counter)
                   print("internalnoe pacpecennie yactot")
                   print ("unterval","     trahin"," chastota")
                        
                 
                        
                    
                       
      
        
        
        
