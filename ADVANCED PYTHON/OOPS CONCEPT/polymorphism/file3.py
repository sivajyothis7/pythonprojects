##method overloading

##same method name also same number of arguments


class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("inside class A",self.num1+self.num2)

class Add2(Add):
    def sum(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print("inside class B",self.no1+self.no2)

ob=Add2()
ob.sum(6,4)  #child class will over write parent class here