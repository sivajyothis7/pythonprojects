#**args : add key/header to multiple values

#kwargs : key word argument

def printvalue(**args):
    return args

print(printvalue(empid=101,fname="vinay",lname="k",age=26,prof="bigdata",salary=1000))