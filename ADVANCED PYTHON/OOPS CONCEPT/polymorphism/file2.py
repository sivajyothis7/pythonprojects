#method overloading #python doesn't support this method,it only support last/latest method

#same method name but different number of arguments

class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)

class Add1(Add):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)

ob=Add1()
ob.sum(4,5,6)
