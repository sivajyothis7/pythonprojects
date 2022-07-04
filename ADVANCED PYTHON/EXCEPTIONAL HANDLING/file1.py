#exceptional handling

num1=int(input("enter  number1"))
num2=int(input("enter number2"))

print(num1/num2)

#to overcome unexpected errors related to input section of code , we use exception handling.

#3 blocks

#try : exception veraaan chance ulla code,try de akath add cheyum
#except : solution in except block
#finally :

num1=int(input("enter  number1"))
num2=int(input("enter number2"))

try:
   print(num1/num2)
except:
   print("zero division error")
finally:
    print("inside")
