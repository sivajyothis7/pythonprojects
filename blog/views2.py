from blog.models import users,posts

def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data

session={}

class signinview:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("login success")
            session["user"]=username
        else:
            print("invalid credentials")



def login(fn):
    def inner_login(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must login")
    return inner_login()



class Postlistview:
    @login
    def get(self,*args,**kwargs):
        return posts

class Mypost:
    @login
    def get(self,*args,**kwargs):
        username=session.get("user")
        user_id=[user["id"] for user in users if users["name"]==username]
        return user_id

sign=signinview()
sign.post(username="Bret",email="Sincere@april.biz")

postlist=Postlistview()
all_posts=postlist.get()
for i in all_posts:
    print(i)

class Mypostview:
    @login_required
    def get(self,*args,**kwargs):
        username=session.get("user")
        userID=[user["id"] for user in users if user["name"]==username]
        print(userID)
