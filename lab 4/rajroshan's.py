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
#sample=[]    
with open('sample_'+surname+ ".csv","r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print("sample before append",sample)
        sample.append(int(row[0]))
        print(sample)
        print("value of sample",sample)  #tested the value must not be zero
        print()
        ranges_num = 8
        sample_sorted = sorted(sample)
        print("value of sample_sorted",sample_sorted)  #tested the value must not be zero
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
                print("value of min sam",min_smpl)  #tested the value must not be zero
                max_smpl =max(sample_sorted)
                print("value of max sam",max_smpl)  #tested the value must not be zero
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
                bottom_bounds=[]
                for i in range(min_smpl, max_smpl, len_int):
                    bottom_bounds.append(i)
                    upper_bounds=[]
                    for i in range(1,len(bottom_bounds)):
                        upper_bounds.append(bottom_bounds[i] - 1)
                    last_bottom_bound= bottom_bounds[len(bottom_bounds) - 1]
                    upper_bounds.append(last_bottom_bound + len_int - 1)
                    prop_bottom_bounds = list()
                    prop_upper_bounds = list()
                    for i,j in zip (bottom_bounds,upper_bounds):
                        prop_upper_bounds.append(i-0.5)
                        prop_upper_bounds.append(j+0.5)

                    int_freq = list()
                    for bot,up in zip(prop_bottom_bounds,prop_upper_bounds):
                        counter = 0
                        for i in sample_sorted:
                            if bot < i < up:
                                counter += 1
                        int_freq.append(counter)
                        print("internalnoe pacpecennie yactot")
                        print ("unterval","     trahin"," chastota")
                        for i,j,k,h,m in zip(bottom_bounds,upper_bounds,prop_bottom_bounds,prop_upper_bounds,int_freq):
                                divider=" | "
                                if i < 10:
                                    sift_bt= " "
                                else:
                                    shift_bt= ""
                                if j<10:
                                    shift_up=" "
                                else:
                                    shift_up=""
                                if k<10:
                                    shift_bt_prc=" "
                                else:
                                    shift_bt_prc= ""
                                if h<10:
                                    shift_up_prc=" "
                                else:
                                    shift_up_prc=""
                                print(shift_bt,i,shift_up,j,divider,shift_bt_prc,k,shift_up_prc,h,divider,m)
                                    
                 
                        
                    
#print (a)
# from math import ceil, floor
# import csv
# import statistics as st #import statistics module under st


# smpl_mode = st.mode(sample_sorted) #mode
# smpl_mode = st.mean(sample_sorted) #mean
# smpl_median = st.median(sample_sorted) #medain

# print()
# print("central parameter: ")
# print("MODE: ",smpl_mode)
# print("median: ",smpl_median)
# print("mean: ", smpl_mean)

      





                       

        
        
        
