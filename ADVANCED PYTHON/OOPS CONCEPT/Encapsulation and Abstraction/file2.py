class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def printvalue(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self,age):
        self.__age=age

pe=Person("arun",25)
pe.printvalue()

pe.setAge(38)
pe.getAge()