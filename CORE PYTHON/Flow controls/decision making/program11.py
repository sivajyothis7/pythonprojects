#largest among 3 numbers

num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

if(num1>num2>num3):
    print(num1)

elif(num2>num1>num3):
    print(num2)

else:
    print(num3)


#OR

num1=int(input("enter number1"))
num2=int(input("enter number2"))
num3=int(input("enter number3"))

if(num1>num2)&(num1>num3):
    print("largest number is number1",num1)

elif(num2>num1&(num2>num3)):
    print("largest number is number2",num2)

else:
    print("largest number is number3",num3)



