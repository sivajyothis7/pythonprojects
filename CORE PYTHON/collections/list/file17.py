#list slicing

lst=[35,20,13,1,2,5,6,8,11,12,15,17,40]

print(lst[1:4])  #lst[1],lst[2],lst[3]...[20,13,1]

print(lst[3:8])  #lst[3],lst[4],lst[5],lst[6],lst[7]

print(lst[:7])   #lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6]

print(lst[3:])   #lst[3] to end of list

print(lst[:])    #will print entire list

#negative index

#[-1 to -n]

print(lst[-1]) #40
print(lst[-3]) #15
print(lst[-6]) #8

print(lst[-4:-1]) #lst[-4], lst[-3], lst[-2] .. [12,15,17]
print(lst[-3:])
print(lst[:-4])