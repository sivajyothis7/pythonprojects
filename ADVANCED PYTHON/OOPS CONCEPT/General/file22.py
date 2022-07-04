#merge list & dic

employee=['vinay','anu']
default={"designation":'bigdata',"salary":1000}

# {'vinay':{"designation":'bigdata',"salary":1000},'anu':{"designation":'bigdata',"salary":1000}}

#fromkeys: it return a dictionary with specified keys and specified values

res=dict.fromkeys(employee,default)
print(res)

print(res['vinay'])
