#map  ==> # output corresponding to every element



#lst=[1,2,3,4,5,6,7,8,9,10] ==> f(x) ==> [1,4,,9,16,25,36,49,64,81,100]

#[ab,ac,ce,df,gh,ip,is] ===> [AB,AC,CE,DF,GH,IP,IS]


#filter - #output for element satisfying condition

#[1,2,3,4,5,6] ===>  f(x) ==> [2,4,6] #even numbers

#syntax

#variable_name=list(map(argument1,argument2)
#variable_name=list(filter(argument1,argument2)

#argument1 ==> function
#argument2 ==> iterable

#find square using map

lst=[1,2,3,4,5,6,7,8,9,10]

def square(num):
    res=num**2
    return res

data=list(map(square,lst))
print(data)

#OR

lst=[1,2,3,4,5,6,7,8,9,10]

data=list(map(lambda num:num**2,lst))
print(data)

#filter example - even number

lst=[1,2,3,4,5,6,7,8,9,10]
def even(num):
    return num%2==0

data=list(filter(even,lst))
print(data)

#OR

lst=[1,2,3,4,5,6,7,8,9,10]

data=list(filter(lambda num:num%2==0,lst))
print(data)