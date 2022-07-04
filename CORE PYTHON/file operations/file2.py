#Read operation

#if both file in different package

f=open("/CORE PYTHON/file operations/sample1", "r")  #absolute path
for i in f:
    print(i)

#f=open("sample1","r") ===> #if both file in same package

f=open("sample1", "r")
for i in f:
    print(i)