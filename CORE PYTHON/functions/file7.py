#create calculator

#1. addition
#2. substraction
#3. multiplication
#4. division

#enter ur choice
#num1
#num2

def add():
    sum=num1+num2
    print(sum)
def sub():
    sub=num1-num2
    print(sub)
def mul():
    mul=num1*num2
    print(mul)
def div():
    div=num1/num2
    print(div)



print( " 1. addition\n","2. subtraction\n","3. multiplication\n","4. division\n")


choice=int(input("enter ur choice"))
num1=int(input("enter number1"))
num2=int(input("enter number2"))

if(choice==1):
    add()
elif(choice==2):
    sub()
elif(choice==3):
    mul()
elif(choice==4):
    div()
else:
    print("invalid")




