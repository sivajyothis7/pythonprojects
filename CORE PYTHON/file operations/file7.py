f=open("C:/Users/Sivaj/Downloads/customer","r")

for i in f:
     data=i.rstrip("\n").split(",")
     if((data[3]>'50') and (data[-1]=='india')):
          print(data[1:5])

#age above 50 & location india
#print fname,lname,age,location