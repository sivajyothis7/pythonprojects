#set operations

#1. union

#2. intersections

#3. difference

#union ==> combined 2 sets but duplicated values will not be present

st1={1,3,5,7,9}

st2={2,3,4,6,8,9}

st3=st1.union(st2)

print(st3)

#intersection ==> collection of common elements in 2 sets

st1={1,3,5,7,9}

st2={2,3,4,6,8,9}

st3=st1.intersection(st2)
print(st3)

#difference

#A-B ==> element present in set A but not present in setB
st1={1,3,5,7,9}

st2={2,3,4,6,8,9}

st3=st1.difference(st2)
print(st3)

st3=st2.difference(st1)
print(st3)