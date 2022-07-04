def admin_permission(fn):
    def inner_fun(*args,**kwargs):
        user=kwargs.get("user")
        if user.role!="admin":
            raise Exception("permission denied")
        else:
           return fn(*args,**kwargs)
    return inner_fun



class User:
    def setuser(self,username,role):
        self.username=username
        self.role=role
    def printuser(self):
        print(self.username,self.role)

class Addcourse:
    @admin_permission
    def setcourse(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.course=kwargs.get("course")
    def printcourse(self):
        print(self.course)

class Addbatch:
    @admin_permission
    def setbatch(self,*args,**kwargs):
        self.user=kwargs.get("user")
        self.course=kwargs.get("course")
        self.batch=kwargs.get("batch")
    def printbatch(self):
        print(self.batch)

user1=User()
user1.setuser("arun","admin")
user1.printuser()


course1=Addcourse()
course1.setcourse(user=user1,course="python")
course1.printcourse()

batch1=Addbatch()
batch1.setbatch(user=user1,course=course1,batch="april22")
batch1.printbatch()