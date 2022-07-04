num=int(input("enter a number"))
lst=[2,3,4,6,8,9]
for i in lst:
    for j in lst:
        if(i+j==num):
            print(i,j,end=' ')

