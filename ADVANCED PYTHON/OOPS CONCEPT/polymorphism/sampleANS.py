
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def print(self):
        print(self.name,self.age,self.place)

f=open("sample","r")

for i in f:
    data=i.rstrip("\n").split(',')

    name=data[0]
    age=data[1]
    place=data[2]

    ob=Person(name,age,place)

    ob.print()

