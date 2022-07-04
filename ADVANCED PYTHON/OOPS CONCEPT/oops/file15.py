#class1 - Person
#attribute - name,age

#class2 - Child
#attribute-place,school

#class3 - student
#attribute - roll,dept,college

#print - name,age,place,dept,college

class person:
    def setperson(self,name,age):
     self.name=name
     self.age=age

class child(person):
    def setchild(self,place,school):
        self.place=place
        self.school=school

class student(child):
    def setstudent(self,roll,dept,college):
        self.roll=roll
        self.dept=dept
        self.college=college
        print(self.name,self.age,self.place,self.dept,self.college)

st=student()
st.setperson("arun",24)
st.setchild("kochi","donbosco")
st.setstudent(101,"python","luminar")

