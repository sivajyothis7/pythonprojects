lst=[4,5,10,12,20]

#lst=[47,46,41,39,31]
#[51] [51-4=47 51-5=46 51-10=41 51-12=39 51=20=31]


lst1=[]
total=(sum(lst))
for i in lst:
    res=total-i
    lst1.append(res)
print(lst1)

