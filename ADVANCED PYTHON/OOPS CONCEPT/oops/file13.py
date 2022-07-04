#class 1- person
#attribute - name,age
#class 2 - parent
#attribute - place ,phone no
#class 3 - employee
#attribute - id,designation,salary

class Person:
    def printa(self,name,age):
        self.name=name
        self.age=age

class Parent:
    def printb(self,place,phone):
        self.place=place
        self.phone=phone

class Employee(Person,Parent):
    def printc(self,ID,designation,salary):
        self.ID=ID
        self.designation=designation
        self.salary=salary
        print(self.name,self.age,self.place,self.phone,self.ID,self.designation,self.salary)

em=Employee()
em.printa("arun",25)
em.printb("kochi",9809302020)
em.printc(101,"python",23000)

