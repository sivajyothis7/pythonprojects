#multiple inheritance with constructor

#Person [name,age,place]
#employee [Id,dept,salary]
#student [roll,college]

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

class Employee:
    def __init__(self,ID,dept,salary):
        self.ID=ID
        self.dept=dept
        self.salary=salary

class Student(Person,Employee):
    def __init__(self,roll,college,name,age,place,ID,dept,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,ID,dept,salary)
        self.roll=roll
        self.college=college
    def printstudent(self):
        print(self.name,self.age,self.place,self.ID,self.dept,self.salary,self.roll,self.college)


ob=Student("arun",24,"kochi",101,"bigdata",25000,111,"luminar")
ob.printstudent()


#single_inheritance

