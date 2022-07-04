#class luminar

#name,roll,age,institution_name,fees

class luminar:
    institution="luminar"
    fees=30000
    def setvalue(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def printvalue(self):
        print(self.name,self.roll,self.age,luminar.institution,luminar.fees)


st1=luminar()
st1.setvalue("siva",101,24)
st1.printvalue()

st2=luminar()
st2.setvalue("tinu", 111, 23)
st2.printvalue()

st3=luminar()
st3.setvalue("steewo", 100,24)
st3.printvalue()

