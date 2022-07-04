class Employee:
    def __init__(self,ID,fname,lname,age,prof,location):
        self.ID=ID
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.location=location

    def print(self):
       print(self.ID,self.fname,self.lname,self.age,self.prof,self.location)

f=open("C:/Users/Sivaj/Downloads/customer","r")


for i in f:
    data=i.rstrip("\n").split(',')
    ID=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    location=data[-1]

    ob=Employee(ID,fname,lname,age,prof,location)
    #ob.print() #to print all arguments

    #append fname,lname,age,prof to list
    lst = []
    lst.append([ob.fname,ob.lname,ob.age,ob.prof])
    print(lst)

    #if we need only fname
    #print(ob.fname)