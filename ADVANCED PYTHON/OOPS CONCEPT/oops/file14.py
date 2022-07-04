#Multi-level Inheritance

class A:
    def printa(self):
        print("Inside class A")
class B(A):
    def printb(self):
        print("Inside class B")
class C(B):
    def printc(self):
        print("Inside class C")

ob=C()
ob.printa()
ob.printb()
ob.printc()

#C inherit B,also B inherit A,So all will be printed.