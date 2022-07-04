#wordcount ==> important

line='cat rat bus cat car car rat bus car car bus cat'

data=line.split(' ')
print(data)

dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)

