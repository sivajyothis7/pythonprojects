#nested list

lst=[[101,'arun','k',26,'bigdata',1000],
     [102,'amal','p',27,'python',1500],
     [103,'vishnu','e',24,'bigdata',1250],
     [104,'anoop','m',27,'python',2000],
     [105,'hari','r',25,'bigdata',1750],
     [106,'vinay','s',28,'bigdata',1500]]

print(lst)

for i in lst:
    print(i)

#fname,lname,age,proffesion

for i in lst:
    print(i[1],i[2],i[3],i[4])
#or
    print(i[1:5])

#age above 25 fname,lname,age,prof,salary

for i in lst:
    if(i[3]>25):
        print(i[1:6])

#fname,lname,age,salary ===> bigdata persons

for i in lst:
    if (i[4]=='bigdata'):
        print(i[1],i[2],i[3],i[5])

#salary above 1750 and age above 25 ==> fname,lstname,age,prof,salary

for i in lst:
    if (i[5]>1750)and(i[3]>25):
        print(i[1:6])

#total salary

sum=0
for i in lst:
    sum+=i[5]
print(sum)
