lst=[1,5,7,8,3,6,2,9,15,20]
lst.sort()
print(lst)
num=int(input("enter a element"))
low=0
upp=len(lst)-1

flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(num<lst[mid]):
        upp=mid-1
    elif(num>lst[mid]):
        low=mid+1
    elif(num==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("element not found")





