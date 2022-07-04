f=open("C:/Users/Sivaj/Downloads/customer","r")
dic={}

for i in f:
    data=i.rstrip("\n").split(",")
    location=data[-1]
    if location not in dic:
        dic[location]=1
    else:
        dic[location]+=1
print(dic)
for k,v in dic.items():
    print(k,",",v)