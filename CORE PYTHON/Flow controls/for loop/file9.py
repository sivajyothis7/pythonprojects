#check given number is prime or not

#2,3,5,7,11,13...

#9 (2,8)
#13 (2,12)

num=int(input("enter a number"))
flg=0
for i in range(2,num):
    if(num%i==0):
       flg=1
       break

if(flg>0):
    print(num,"is not prime")
else:
    print(num,"is prime")

