st={1,5,5,10,10,14,15,15,20,25}

print(st)

#remove ==> to delete element from set

st.remove(20)
print(st)

#OR

#discard

st.discard(5)
print(st)

#diff. b/w remove & discard

#remove has return type
#discard has no return type

st={1,5,5,10,10,14,15,15,20,25}
print(st)
st.remove(50)
print(st)
st.discard(50)
print(st)