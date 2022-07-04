num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

#NESTEDIF PROBLEM

if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("2nd largest is",num2)
    else:
        print("2nd largest is",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("2nd largest is",num1)
    else:
        print("2nd largest is",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("2nd largest is",num1)
    else:
        print("2nd largest is",num2)

else:
    print("INVALID")