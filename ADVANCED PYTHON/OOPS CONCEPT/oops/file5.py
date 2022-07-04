#employee
#name,ID,designation,salary,company

class Employee:
    def setvalue(self,name,ID,designation,salary,company):
        self.name=name
        self.ID=ID
        self.designation=designation
        self.salary=salary
        self.company=company
    def printvalue(self):
        print(self.name,self.ID,self.designation,self.salary,self.company)


em1=Employee()
em1.setvalue("arun",10,"python",15000,"luminar")
em1.printvalue()


em2=Employee()
em2.setvalue("amal",15,"bigdat",25000,"infopark")
em2.printvalue()


em3=Employee()
em3.setvalue("mowlu",45,"python",55000,"luminar")
em3.printvalue()