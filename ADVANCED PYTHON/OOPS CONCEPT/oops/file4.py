#student
#name,rollno,department,college_name

class Student:
    def setvalue(self,name,rollno,department,college):
        self.name=name
        self.rollno=rollno
        self.department=department
        self.college=college
    def printvalue(self):
        print(self.name)
        print(self.rollno)
        print(self.department)
        print(self.college)

pe1=Student()
pe1.setvalue("anu",12,"computer","christ")
pe1.printvalue()

pe2=Student()
pe2.setvalue("arun",10,"civil","luminar")
pe2.printvalue()

pe3=Student()
pe3.setvalue("namith",21,"computer","christ")
pe3.printvalue()