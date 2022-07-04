f=open("file15-sample", "r")
special="@#$%"

for i in f:
    data=i.rstrip("\n")
    string=''
    for j in data:
        if j not in special:
            string+=j
print(string)