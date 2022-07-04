#constructor

#objectinte akathu instance variable define cheyyan vendi use cheyunnath
#name,age,place

class Person:
    def __init__(self,name,age,place): #constructor ==>  __init__
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

pe1=Person("arun",25,"kochi")
pe1.printvalue()