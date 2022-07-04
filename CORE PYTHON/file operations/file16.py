f=open("file15-sample", "r")
special="@#$%"
for i in f:
    data=i.rstrip("\n")
    string=''
    for j in data:
        if j not in special:
            string+=j
print(string)

#wordcount

dic={}
data1=string.split(' ')

for i in data1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)


