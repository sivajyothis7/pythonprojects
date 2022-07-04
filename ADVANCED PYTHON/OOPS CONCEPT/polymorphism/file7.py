#inheritance with constructor

#Person [name,age,place]

#student [roll,dept,college]

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def __init__(self,roll,dept,college,name,age,place):
        super().__init__(name,age,place)  #no need of self in 'super'
        self.roll=roll
        self.dept=dept
        self.college=college
    def printstudent(self):
        print(self.roll,self.dept,self.college)

ob=Student("vinay",26,"kochi",101,"python","luminar")

ob.printstudent()
ob.printperson()
