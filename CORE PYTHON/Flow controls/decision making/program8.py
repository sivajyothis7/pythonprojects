cost=int(input("enter cost of bike"))
if(cost>100000):
    print("total tax=",cost*15/100)

elif(50000<cost<=100000):
    print("total tax=",cost*10/100)

else:
    print("total tax=", cost*5/ 100)
