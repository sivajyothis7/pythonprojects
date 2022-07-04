#tuples

#1. How to define

tu=() #paranthesis

tu1=tuple()
print(type(tu))
print(type(tu1))

tu=(10,12,14,16,20)
print(tu)

#2. Heterogeous supported or not

tu1=(10,10,11.5,'python',True,'bigdata')  #==> it supports heterogenous data
print(tu1)

#3. Duplicates allowed or not

tu2=(10,101,15,15,40,40,'python','python')  #==> it supports duplicated values
print(tu2)

#4. insertion order is preserved

#5 tuple is imutable

tu2[3]=100
print(tu2)

