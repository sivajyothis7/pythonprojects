#how to create class

#syntax

#class Class_name: #enter first letter with CAPS

#class Person:

#methods - classinte akath nammal define cheyunna functionsintte peraanu methods

class Person:
    def reading(self):  # method1 #self ==> instance keyword
        print("reading books")

    def writting(self):
        print("writting a book")  # method2

pe=Person() #object #==> create object using "class_name"
pe.reading() #reference  # object.function call ==> reference
pe.writting() #reference

pe1=Person()
pe1.writting()

pe2=Person()
pe2.reading()