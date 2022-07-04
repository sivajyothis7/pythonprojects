pattern='ABCDBCDEF'
#print first recursive letter

dic={}

for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print("first recursive letter is",i)
        break

