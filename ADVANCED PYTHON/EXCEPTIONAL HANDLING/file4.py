n1=int(input("enter num1"))
n2=int(input("enter num2"))

try:
    print(n1/n2)
except Exception as e:
    print("error",e)