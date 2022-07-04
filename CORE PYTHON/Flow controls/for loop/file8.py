low=int(input("enter lower limit"))
upp=int(input('enter upper limit'))
even_sum=0
odd_sum=0

for low in range(low,upp+1):
    if(low%2==0):
        even_sum+=low
    else:
        odd_sum+=low

print(even_sum)
print(odd_sum)
    