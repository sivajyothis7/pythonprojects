from blog.models import users

# def autenthicate(username,email):
#
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data
#
# user=autenthicate("Bret","Sincere@april.biz")
# if user:
#     print("login success")
# else:
#     print("invalid credentials")


def autenthicate(**kwargs): #use **kwargs for dictionary format
    username=kwargs.get("username") #use get function to avoid  servor error
    email=kwargs.get("email")
    user_data= [user for user in users if user["username"] == username and user["email"] == email]
    return user_data


user=autenthicate(username="Bret", email="Sincere@april.biz")
if user:
    print("login success")
else:
    print("invalid credentials")