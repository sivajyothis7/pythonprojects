#find cube of a number

def cube():
    num=int(input("enter a number"))
    res=num**3
    print(res)

cube()


def cube(num):
    res=num**3
    print(res)

cube(2)

def cube(num):
    res=num**3
    return res

data=cube(2)
print(data)


