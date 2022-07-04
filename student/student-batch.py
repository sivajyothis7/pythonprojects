class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course_name


class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.student_name



dj=Course()
dj.add_course(course_name="django",status=True)
print(dj)

ms=Course()
ms.add_course(course_name="meanstack",status=True)

djB1=Batch()
djB1.add_batch(course=dj,batch_code="djmay2k22",start_date="12/6/22")
print(djB1)
print(djB1.course)
print(djB1.course.status)

msB1=Batch()
msB1.add_batch(course=ms,batch_code="meanstackapril2k22",start_date="1/5/22")

ajay=Student()
ajay.add_student(student_name="ajay",email="ajay12@gmail.com",batch=djB1)

pappachan=Student()
pappachan.add_student(student_name="pappachan",email="pappachan12@gmail.com",batch=djB1)

vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu12@gmail.com",batch=msB1)

print(vishnu.batch.course)

students=[]
students.append(ajay)
students.append(pappachan)
students.append(vishnu)



ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="django"]
print(ms_stud)