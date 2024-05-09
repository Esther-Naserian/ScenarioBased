class User:
    def __init__(self,username):
       self.username = username
       self.user_id = None
    
class UserSystem:
    def ___init__(self):
        self.users=[]
        self.user_id =1

    def add_user(self,username):
        user = User(username)

        user.user_id= self.user_id_counter
        self.user_id_counter += 1
        self.users.append(user)
    
User_System = UserSystem()
User_System.add_user("Naserian")
User_System.add_user("Samuria")

print("username")
user_followers =[
    {"useename": "user1","followers":["followers","followers2","followers3"]},
    {"username": "user2","followers":["follower4","followers5"]},
    print("username")
]
def get_followers(username):
    for user in user_followers:
        if user["username"]==username:
            return user["followers"]
        else:
            return[]
        print(get_followers(user1))
        print(get_followers("user3"))

    
        