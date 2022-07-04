#lower to upper even numbers

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))

for lower in range(lower,upper+1):
    if(lower%2==0):
        print(lower)
