#name,age,prof,salary

#name ===> fname
#print prof
#company key present or not
#company ==> luminar
#salary +5000
#key-value pairs

dic={"name":'vinay',"age":25,"prof":'python',"salary":10000}

dic["fname"]=dic["name"]
del dic["name"]
print(dic)

print(dic["prof"])
print("company" in dic)
dic["company"]='luminar'
print(dic["company"])
dic["salary"]+=5000
print(dic["salary"])
for i in dic:
    print(i,dic[i])
