lst=[]
lst_even=[]
lst_odd=[]


for i in range(1,76):
    lst.append(i)
print(lst)

for i in lst:
    if(i%2==0):
        lst_even.append(i)

    else:
        lst_odd.append(i)




print(lst_odd)
print(lst_even)
print(sum(lst))
print(sum(lst_even))
print(sum(lst_odd))
