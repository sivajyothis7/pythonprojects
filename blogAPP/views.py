from blogAPP.models import users,posts

#1  #authenticate
    #username
    #password

# username="anu"
# password="Password@123"

# user_data=[user for user in users if user["username"]==username and user["password"]==password]
# print(user_data)

# def authenticate(username,password):
#
#
#     user_data=[user for user in users if user["username"]==username and user["password"]==password]
#     return user_data
#
# print(authenticate("anu","Password@123"))

#3
session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("you must log in")
    return wrapper

#1
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")

    user_data=[user for user in users if user["username"]==username and user["password"]==password]
    return user_data

# print(authenticate(username="anu",password="Password@123"))

#GET ==> retreive
#POST ==> Create
#PUT/PATCH ==> edit
#DELETE ==> delete

#2
class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("login success")
        else:
            print("invalid")

#4

class Postsview:

    @signin_required
    def get(self,*args,**kwargs):

        return posts

    @signin_required
    def post(self,*args,**kwargs):

        userId=session["user"]["id"]
        kwargs["userId"]=userId
        print(kwargs)
        posts.append(kwargs)
        print(posts)


class Mypostlistview:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts


class Postdetailview:

    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post

    @signin_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)
        return post


    @signin_required
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post_delete=data[0]
            posts.remove(post_delete)
            print("post removed")
            print(len(posts))

    @signin_required
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        post_data=self.get_object(post_id)
        if post_data:
            post_update=post_data[0]
            post_update.update(data)
            return(posts)


class Likeview:

    @signin_required
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)



#
log=SignInView()
log.post(username="richard",password="Password@123")
print(session)

# data=Postsview()
# print(data.get())
                                        #createpost

# data.post(postId=9,
#           title="new post",
#           content="qwerty",
#           liked_by= []
#           )

mypost=Mypostlistview()
print(mypost.get())

post_detail=Postdetailview()
# post_detail.delete(post_id=6)
# print(post_detail.get(post_id=4))

data={
        "title":"sukhamano",
        "content":"new_content"
}

print(post_detail.put(post_id=4,data=data))

like=Likeview()
like.get(postid=6)


