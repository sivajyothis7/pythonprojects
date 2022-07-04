#2 class
#person : name,age,place
#student : name,age,place,roll,department



class Person:
    def printa(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)

class Student(Person):
    def printb(self,roll,department):
        self.roll=roll
        self.department=department
        print(self.name,self.age,self.place,self.roll,self.department)

st1=Student()

st1.printa("arun",24,"kochi")
st1.printb(100,"python")
