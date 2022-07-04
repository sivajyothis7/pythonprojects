dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"marks":30}
print(dic)

#corresponding key is used to collect single value of dictionary

print(dic["marks"])
print(dic["name"])
print(dic["dept"])

#marks ==> 30 to 50

dic["marks"]=50  #or
print(dic)
dic["marks"]+=20
print(dic)
dic["name"]='sabir'
print(dic)

#key:value #To add new key value pairs

dic["total"]=150
print(dic)

del dic["roll"] #to delete key value pair
print(dic)