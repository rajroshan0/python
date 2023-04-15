import math
print(math.floor(2.4));
print(math.floor(42342.43432));
print(math.ceil(5236.63545));

i=0
rajroshan=['red','orange','green','cyan','blue','violet']
for color in rajroshan:
    print('#', i, ' color of rainbow is ', color, sep ='+')
    i += 1

my_lst = [1,3,3,5,2,5]
for i in my_lst:
    print(i)

for i in range(0,4):
    print(i)


for i in range(4,8):
    print(i)
    
for i in range(1,100,4):
    print(i)

zip() # this code execute two list or array at the same time and combine them together

lst_fruit=["apple","orange", "guava","leeche", "pears"]
lst_price = [123,323,1242,44,12]

for i,j in zip(lst_fruit,lst_price):
     print (i,j, sep ='---')
   
    

    

