class Person:
    def setvalue(self,name,age,place):
        self.name=name #self.name is instance argument
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
#oru functionile value vere functionil use cheyan pattila ,so athu overcome cheyaan aanu self keyword
#self keyword is used to change argument to instance argument

pe1=Person()
pe1.setvalue("anu",26,"kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("arun",25,"thrissur")
pe2.printvalue()

