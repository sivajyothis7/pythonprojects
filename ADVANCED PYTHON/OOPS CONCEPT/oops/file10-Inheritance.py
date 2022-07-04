#inheritance

#parent

#child

#child collects features of parents

#class A (parent)
#class B (child)

class A:  #parent class,base class,super class
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)

class B(A): #child class,sub class,derived class
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2,self.num1)

b=B()

b.printa(50)
b.printb(40)