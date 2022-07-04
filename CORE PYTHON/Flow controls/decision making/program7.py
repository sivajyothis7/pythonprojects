classes_held=int(input("enter classes held"))
classes_attended=int(input("enter classes attended"))

percentage=(classes_attended/classes_held)*100
print(percentage)

if(percentage>=75):
    print("you are allowed to sit in exam")

else:
    print("you are not allowed to sit in exam")
