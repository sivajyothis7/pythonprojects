from blog.models import users,posts



def authenthicate(**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data

# user=authenthicate(username="Bret",email="Sincere@april.biz")
# if user:
#     print("login success")
# else:
#     print("invalid")

session={} #if login succes ,store user credentials in dictionary

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
           print("you must login")
    return wrapper

@login_required
def logged_user():
    username=session.get("user")
    userID=[user["id"] for user in users if user["username"] == username][0]
    return userID





class signinview:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        email=kwargs.get("email")
        user=authenthicate(username=username,email=email)
        if user:
            print("success")
            session["user"]=username
        else:
            print("invalid credentials")

@login_required
def logout(*args,**kwargs):
    session.pop("user")



class Postlistview:
    @login_required
    def get(self,*args,**kwargs):
        return posts




# postlist=Postlistview()
# all_posts=postlist.get()
# for i in all_posts:
#     print(i)
#

class Mypostview:
    @login_required
    def get(self,*args,**kwargs):


        userID=logged_user()
        qs=[post for post in posts if post["userId"]==userID]
        return qs

class Postcreateview:
    @login_required
    def post(self,*args,**kwargs):
        userId=logged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")
# logout()
# print(session)
class Specificpostview:
    @login_required
    def get(self,*args,**kwargs):

        id=kwargs.get("id")
        sp=[p for p in posts if p.get("id")==id]
        return sp

    def put(self,id=None,*args,**kwargs):

        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)






sign=signinview()
sign.post(username="Bret",email="Sincere@april.biz")
# print(session)
pst=Postcreateview()
pst.post(title="mypost",body="this is my post")

po=Mypostview()
print(po.get()[-1])

detail=Specificpostview()
print(detail.get(id=5))

detail.put(id=6,title="new post",body="this is my new post")


#print(dir(dict)) = to know keys of dictionary