#factorial

#5 : 1*2*3*4*5
#10 : 1*2*3*4......10


def factorial():
    num=int(input("enter a number"))#3
    fact=1

    for i in range(1,num+1):#1 2
      fact*=i #0*1=0 0*2=0
    print(fact)


factorial()


def factorial(num):
    factorial=1

    for i in range(1,num+1):
        factorial*=i
    print(factorial)

factorial(5)


def factorial(num):
    factorial=1

    for i in range(1,num+1):
        factorial*=i
    return(factorial)

data=factorial(5)
print(data)



