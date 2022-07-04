sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
sub3=int(input("enter sub3 marks"))
sub4=int(input("enter sub4 marks"))

total_marks=sub1+sub2+sub3+sub4

if(total_marks>=180):
    print("your grade is A+")

elif(160<=total_marks<=179):
    print(""your grade is A)

elif(140<=total_marks<=159):
    print("your grade is B+")

elif(120<=total_marks<=139):
    print("your grade is B")

elif(100<=total_marks<=119):
    print("your grade is C+")

elif(80<=total_marks<=99):
    print("your grade is B")

else:
    print("FAIL")