#1. create a list from element of a range from 1200 to 2000 with steps of 130

#2. lst=[44,54,64,74,104]

#lst1=[50,60,70,80,110]

#3. create 1 to 15 list and print data of elements square greater than 50

lst=[i for i in range(1200,2001,130)]
print(lst)

lst=[44,54,64,74,104]
lst1=[i+6 for i in lst]
print(lst1)

lst=[i for i in range(1,16) if i**2>50]
print(lst)