f=open("numbers", "r")


lst=[]
for i in f:
    lst.append(int(i.rstrip("\n")))

print(lst)
print(sum(lst))

#\n in output==> for every line \n will come in output

#rstrip ==> to remove right side character

# line="hello\n"
# data=line.rstrip("\n")
# print(data)