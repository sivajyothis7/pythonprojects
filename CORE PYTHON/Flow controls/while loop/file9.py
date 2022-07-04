low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))




even_sum=0
odd_sum=0
while(low<=upp): #1<10
    if (low % 2 == 0):
     even_sum+=low
    else:
     odd_sum+=low
    low+=1

print(even_sum)
print(odd_sum)

