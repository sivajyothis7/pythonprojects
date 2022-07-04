salary=int(input("enter your salary"))
year=int(input("enter your year of service"))
bonus=salary*0.05
if(year>5):
    print("net bonus=",bonus)
    print("your bonus salary is",salary+bonus)
else:
    print("you are not eligible for bonus")


salary=int(input("enter your salary"))
year=int(input("enter your year of service"))

if(year>5):
    print("net bonus=",salary*0.05)
    
else:
    print("you are not eligible for bonus")
