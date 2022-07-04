class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printa(self):
        print("inside class B")

ob=B()
ob.printa()

class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printa(self):
        print("inside class B")
class C(B):
    def printa(self):
        print("inside class C")

ob1=C()
ob1.printa()