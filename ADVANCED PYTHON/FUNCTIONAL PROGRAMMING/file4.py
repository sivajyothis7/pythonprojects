#list-comprehension

lst=[]
for i in range(1,101):
    lst.append(i)

print(lst)

#syntax1

#lst=[print range]

lst=[i for i in range(1,101)]
print(lst)

#add 1 to 75 and print(1,5,9,13,17...75)

lst=[i for i in range(1,75,4)]
print(lst)

#1 to 100 even numbers

#syntax2

#lst=[print range condition]

lst=[i for i in range(1,101) if i%2==0]
print(lst)

#1 to 50 odd numbers

lst=[i for i in range(1,51) if i%2!=0] #or i%2==1
print(lst)

lst=[(i,'even') for i in range(1,101) if i%2==0]
print(lst)

#syntax 3 ==> when more than 1 conditions are present

#[print if condition else print range]

#[print1 if condition1 else print2 if condition else print3 range]

#[print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range]

#1-50

#print square of even numbers
#print cube of odd numbers

lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
print(lst)

##print square of even numbers
#print odd numbers

lst=[i**2 if i%2==0 else i for i in range(1,51)]
print(lst)

lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst)