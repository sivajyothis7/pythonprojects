class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def printvalue(self):
        print(self.name,self.__age)

pe=Person("arun",25)
pe.printvalue()

print(pe.name)
print(pe.__age)