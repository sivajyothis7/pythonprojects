#calculate sum

def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(1,4,5))