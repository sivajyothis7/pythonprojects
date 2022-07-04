#even
#odd

#1-30

lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,31)]
print(lst)