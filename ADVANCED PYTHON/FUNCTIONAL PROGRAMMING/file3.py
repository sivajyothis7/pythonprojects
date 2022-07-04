#add 1 to every element in list

lst=[1,2,3,4,5,6,7,8,9,10]

def res(num):
    return num+1

data=list(map(res,lst))
print(data)

#OR


lst=[1,2,3,4,5,6,7,8,9,10]
data=list(map(lambda num:num+1,lst))
print(data)