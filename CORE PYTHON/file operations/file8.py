#each profession count

f=open("C:/Users/Sivaj/Downloads/customer","r")
dic={}
for i in f:
    data = i.rstrip("\n").split(",")

    prof=data[4]


    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)

for k,v in dic.items():
    print(k,",",v)