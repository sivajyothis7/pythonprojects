#print subject with lowest marks

dic1={
    'physics':56,
    'maths':65,
    'history':80
}

print(dic1)

#lowest subject

print(min(dic1,key=dic1.get))