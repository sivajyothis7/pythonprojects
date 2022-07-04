dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"marks":30}

for i in dic:
    print(i,dic[i])

print("name" in dic) #true
print("total" in dic) #false
print("roll" not in dic) #false