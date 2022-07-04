#Dictionary

#1. How to define

dic={}

print(type(dic))

#key-value pairs

#roll:101
#name:vinay
#age:26
#dept:bigdata
#salary:1000

#key=roll,name,age,dept,salary
#pair=101,vinay,26,bigdata,1000

dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"salary":1000}
print(dic)

#2. Heterogenous data is supported

#3. duplicated value supported or not

dic={"roll":101,"name":'vinay',"age":26,"marks":26}
print(dic)
dic={"roll":101,"name":'vinay',"age":26,"age":26}
print(dic)
#duplicate values are supported but duplicate KEY are not supported

#4. insertion order is preserved
#5. dictionary is mutable