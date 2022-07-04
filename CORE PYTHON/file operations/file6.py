
f=open("C:/Users/Sivaj/Downloads/customer","r")

# for i in f:
#     data=i.rstrip("\n").split(",")
    # print(data)
    #fname,lname,age
    # fname=data[1]
    # lname=data[2]
    # age=data[3]
    # # print(fname,",",lname,",",age)
    # print(data[1],data[2],data[3])
    # print(data[1:4])
    # print(data[0:5:2])

for i in f:
     data=i.rstrip("\n").split(",")
     if(data[3]>'50'):
         print(data[1],data[2],data[3],data[4])



