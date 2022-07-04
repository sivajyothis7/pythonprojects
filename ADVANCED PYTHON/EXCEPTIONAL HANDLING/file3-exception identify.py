lst=[1,2,3,4]
i=int(input("enter a index"))

try:
    print(lst[i])
except Exception as e:
    print("exception occured",e)