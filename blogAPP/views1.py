from blogAPP.models import users,posts

#authentication

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user_data=[user for user in users if user["username"]==username and user["password"]==password]
    return user_data

# print(authenticate(username="akhil",password="Password@123"))

#login
session={}
class Signin:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            print("login success")
            session["user"]=user[0]
        else:
            print("Invalid credentials")

login=Signin()
login.post(username="akhil",password="Password@123")
print(session)

#postview:
